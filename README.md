Метою цього проєкту є розробка ефективного діалогового компоненту віртуального асистента з використанням мереж Петрі для підвищення точності розпізнавання намірів користувача та релевантності згенерованих відповідей.
This project aims to develop an effective dialog component of a virtual assistant using Petri nets to improve the accuracy of recognizing user intentions and the relevance of generated responses.

Розроблений діалоговий компонент має широкі можливості для практичного застосування в різних сферах, включаючи бізнес, освіту та охорону здоров'я. Його впровадження може значно підвищити якість обслуговування клієнтів та ефективність роботи віртуальних асистентів.
The developed dialogue component has wide possibilities for practical application in various fields, including business, education, and healthcare. Its implementation can significantly improve the quality of customer service and the efficiency of virtual assistants.

Основою системи є клас PetriNet, який реалізує функціональність мережі Петрі.
The basis of the system is the PetriNet class, which implements the functionality of the Petri net.

Система реалізована з використанням мови програмування Python та веб-фреймворку Flask, що забезпечує легку інтеграцію та розгортання.
The system is realized using the Python programming language and the Flask web framework, which ensures easy integration and deployment.

Конфігурація системи, включаючи переходи, ключові слова та відповіді, зберігається у файлі responses.json. Це JSON-файл, який містить два основних розділи: "transitions" та "responses". Розділ "transitions" визначає переходи мережі Петрі та пов'язані з ними ключові слова. Розділ "responses" містить відповіді, які система може надати на основі активованих переходів.
The system configuration, including transitions, keywords, and responses, is stored in the responses.json file. This JSON file contains two main sections: “transitions” and “responses.” The “transitions” section defines the Petri nets transitions and associated keywords. The “responses” section contains the responses that the system can provide based on the activated transitions.

Веб-інтерфейс системи реалізований за допомогою Flask. Основний маршрут ('/') відображає головну сторінку, де користувач може ввести свій запит. Обробка запиту відбувається через маршрут '/process_input', який приймає POST-запити.
The system's web interface is implemented using Flask. The main route ('/') displays the main page where users can enter their requests. The request is processed through the '/process_input' route, which accepts POST requests.

Віртуальний асистент має модуль «Адміністрування». Він надає змогу завантажити файл формату csv, який містить додаткові знання для віртуального асистента. Таким чином, надаючи користувачу або оператору системи постійно вдосконалювати його можливості. Також, користувач на даній сторінці має змогу натиснути кнопку «Згенерувати звіт». У відповідь система надасть змогу завантажити звіт, у форматі CSV, який буде відображати поточний набір знань віртуального асистента.
The virtual assistant has an Administration module. It allows you to download a CSV file that contains additional knowledge for the virtual assistant. Thus, it allows the user or system operator to constantly improve its capabilities. Also, the user can click the “Generate report” button on this page. In response, the system will provide an opportunity to download a report in CSV format, which will reflect the current set of knowledge of the virtual assistant.

! Інструкція. Завантажте всі файли з репозиторію, відкрийте їх через програмне середовище (наприклад, VS Code), оберіть файл "main.py" та відкрийте його в терміналі, далі впишіть команду "python main.py", натисніть enter. В результаті з'явиться посилання "http://127.0.0.1:5000", перейдіть за ним, і нарешті віртуальний асистент перед Вами готовий до співпраці.
! How to install. Download all the files from the repository, open them through a software environment (for example, VS Code), select the file “main.py” and open it in the terminal, then type the command “python main.py”, and press enter. As a result, you will see the link “http://127.0.0.1:5000”, click on it, and finally, the virtual assistant in front of you is ready to cooperate.
