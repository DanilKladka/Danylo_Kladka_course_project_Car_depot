#Імпортуємо бібліотеки які нам знадобляться та підключаємо БД
import sys
import mysql.connector
from PyQt5.QtWidgets import QApplication
from start_page import StartPage

# Встановлюємо з'єднання з БД MySQL
connectToDB = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "12345678",
            database = "cardepot")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Створення екземпляра класса StartPage та передаємо в якості параметра підключення до БД
    main_window = StartPage(connectToDB)
    main_window.show()
    sys.exit(app.exec_())