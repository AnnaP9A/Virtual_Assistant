import json
import csv
import io
from flask import Flask, render_template, request, jsonify,  send_file

# Клас для представлення мережі Петрі
class PetriNet:
    def __init__(self):
        self.places = {}  # Місця з кількістю токенів
        self.transitions = {}  # Переходи з відповідними місцями

    def add_place(self, place_name):
        if place_name not in self.places:
            self.places[place_name] = 0  # Ініціалізуємо місце з 0 токенами

    def add_transition(self, transition_name):
        if transition_name not in self.transitions:
            self.transitions[transition_name] = []  # Ініціалізуємо перехід з пустим списком місць

    def add_arc(self, place_name, transition_name):
        if place_name in self.places and transition_name in self.transitions:
            self.transitions[transition_name].append(place_name)  # Додаємо дугу між місцем та переходом

    def fire_transition(self, transition_name):
        if transition_name in self.transitions:
            for place_name in self.transitions[transition_name]:
                if self.places[place_name] > 0:
                    self.places[place_name] -= 1  # Зменшуємо кількість токенів у місці
                else:
                    raise Exception(f"Недостатньо токенів у місці {place_name} для запуску переходу {transition_name}")
        else:
            raise Exception(f"Перехід {transition_name} не існує в мережі Петрі")

# Завантажуємо відповіді з JSON-файлу
with open('responses.json', 'r', encoding='utf-8') as f:
    responses_data = json.load(f)

# Ініціалізація Flask додатку
app = Flask(__name__)
petri_net = PetriNet()

# Ініціалізація мережі Петрі з даних JSON
for transition in responses_data['transitions']:
    petri_net.add_transition(transition)

# Маршрути
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/process_input', methods=['POST'])
def process_input():
    input_text = request.form['user_input'].lower().strip()
    response = ""

    print(f"Отриманий вхідний текст: {input_text}")

    # Логіка мережі Петрі
    for transition, keywords in responses_data['transitions'].items():
        if any(keyword in input_text for keyword in keywords):
            print(f"Знайдено відповідність переходу: {transition} з ключовими словами: {keywords}")
            try:
                petri_net.fire_transition(transition)
                print(f"Перехід {transition} успішно запущено.")
            except Exception as e:
                response = responses_data['responses']['error'].format(error=str(e))
                return jsonify({"response": response}), 400

            # Генерація відповіді
            response = next((responses_data['responses'].get(keyword) for keyword in keywords if keyword in input_text), responses_data['responses']['default'])
            return jsonify({"response": response}), 200

    # Відповідь за замовчуванням, якщо немає відповідного переходу
    response = responses_data['responses']['default']
    print(f"Не знайдено відповідного переходу. Відповідь за замовчуванням: {response}")
    return jsonify({"response": response}), 200

# Admin page for uploading CSV
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    messages = []
    
    if request.method == 'POST':
        print("POST request received with file:", request.files)
        # Check if the POST request has the file part
        if 'file' not in request.files:
            messages.append("No file part in the request")
            return render_template('admin.html', messages=messages)

        file = request.files['file']

        # Check if a file was selected
        if file.filename == '':
            messages.append("No selected file")
            return render_template('admin.html', messages=messages)

        # Process the file if it exists and is valid
        if file and file.filename.endswith('.csv'):
            try:
                # Read and decode the file
                csvfile = file.stream.read().decode('utf-8').splitlines()
                reader = csv.DictReader(csvfile)

                # Update responses.json
                for row in reader:
                    transition = row['transition']
                    keyword = row['keyword']
                    response = row['response']

                    # Update the transitions and responses in the JSON
                    if transition not in responses_data['transitions']:
                        responses_data['transitions'][transition] = []
                    responses_data['transitions'][transition].append(keyword)
                    responses_data['responses'][keyword] = response

                # Write the changes to responses.json
                with open('responses.json', 'w', encoding='utf-8') as f:
                    json.dump(responses_data, f, ensure_ascii=False, indent=4)

                messages.append("Дані з CSV файлу успішно додані до responses.json.")
                return render_template('admin.html', messages=messages)
            except Exception as e:
                messages.append(f"Error processing CSV: {str(e)}")
                return render_template('admin.html', messages=messages)

    return render_template('admin.html', messages=messages)

# Route to generate and download the report
@app.route('/generate_report', methods=['GET'])
def generate_report():
    # Create an in-memory binary file to store the CSV data
    output = io.StringIO()  # Use StringIO for text output
    writer = csv.writer(output)

    # Write header
    writer.writerow(['Transition', 'Keywords', 'Response'])

    # Write the data from responses.json
    for transition, keywords in responses_data['transitions'].items():
        for keyword in keywords:
            response = responses_data['responses'].get(keyword, 'No response found')
            writer.writerow([transition, keyword, response])

    # Get the CSV data as a string
    output.seek(0)  # Move to the beginning of the StringIO buffer
    return send_file(io.BytesIO(output.getvalue().encode('utf-8')),
                     mimetype='text/csv',
                     as_attachment=True,
                     download_name='report.csv')

if __name__ == '__main__':
    app.run(debug=True)
