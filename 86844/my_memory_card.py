#создай приложение для запоминания информации
from PyQt5.QtWidgets import QApplication, QWidget
import sys 
from Window import My_Window
if __name__ == '__main__':
    app = QApplication([])
    window = My_Window()
    window.show()
    sys.exit(app.exec_())