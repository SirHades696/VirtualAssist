import sys
from VirtualAssistGUI import *
from alex import Alex

class Asistente(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def run_alex(self):
        self.state_button(flag = False)
        text = ''
        text += 'Bienvenido al servicio de Alex, te escucho\n'
        self.ui.text.setText(text)
        self.assis.talking_alex('Bienvenido al servicio de Alex, te escucho')
        while True:
            try:
                self.assis.virtual_assist(text)
            except UnboundLocalError:
                text += 'No dectecte ningun comando, deteniendo el servicio'
                self.ui.text.setText(text)
                self.assis.talking_alex('No dectecte ningun comando, deteniendo el servicio')
                self.state_button(flag = True)
                break

    def action_btn(self):
        self.assis = Alex(self.ui.text)
        self.ui.button.clicked.connect(self.run_alex)

    def state_button(self, flag):
        if flag == True:
            self.ui.button.setEnabled(True)
            self.ui.button.setStyleSheet("QPushButton#button{font-size:15px;border-radius: 15px;"
            "background:} QPushButton#button:hover{font-size:15px;border-radius: 15px;background:#2b5797;}")
        else:
            self.ui.button.setEnabled(False)
            self.ui.button.setStyleSheet("background:gray")
    
    def close_window(self):
        exit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    MainWindow = Asistente()
    MainWindow.show()
    MainWindow.action_btn()
    app.lastWindowClosed.connect(MainWindow.close_window)
    sys.exit(app.exec_())
