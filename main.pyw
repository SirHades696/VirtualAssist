import sys
from VirtualAssistGUI import *
from alex import Alex

class Asistente(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def run_alex(self):
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
                break

    def action_btn(self):
        self.assis = Alex(self.ui.text)
        self.ui.button.clicked.connect(self.run_alex)
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Asistente()
    MainWindow.show()
    MainWindow.action_btn()
    sys.exit(app.exec_())