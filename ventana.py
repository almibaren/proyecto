from ventana_ui import *

tablero = [];
negras = [];
blancas = [];


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.miTurno=False;
        self.setupUi(self)
        self.crearArraysTablero();
        self.crearFichasNegras();
        self.crearFichasBlancas();
        self.deshabilitarBotones();
        self.buttonPasar.clicked.connect(self.habilitarDeshabilitarBlancas);


    def habilitarDeshabilitarBlancas(self):
        if self.miTurno == False:
            for button in blancas:
                button.setEnabled(True);
            self.miTurno=True;
        else:
            self.deshabilitarBotones();
            self.miTurno=False;
    def deshabilitarBotones(self):
        for button in tablero:
            button.setEnabled(False);


    def actualizar(self):
        self.button33.setText("¡Acabas de hacer clic en el botón!")

    def crearArraysTablero(self):
        tablero.append(self.button11)
        tablero.append(self.button12)
        tablero.append(self.button13)
        tablero.append(self.button14)
        tablero.append(self.button15)
        tablero.append(self.button16)
        tablero.append(self.button17)
        tablero.append(self.button18)
        tablero.append(self.button21)
        tablero.append(self.button22)
        tablero.append(self.button23)
        tablero.append(self.button24)
        tablero.append(self.button25)
        tablero.append(self.button26)
        tablero.append(self.button27)
        tablero.append(self.button28)
        tablero.append(self.button31)
        tablero.append(self.button32)
        tablero.append(self.button33)
        tablero.append(self.button34)
        tablero.append(self.button35)
        tablero.append(self.button36)
        tablero.append(self.button37)
        tablero.append(self.button38)
        tablero.append(self.button41)
        tablero.append(self.button42)
        tablero.append(self.button43)
        tablero.append(self.button44)
        tablero.append(self.button45)
        tablero.append(self.button46)
        tablero.append(self.button47)
        tablero.append(self.button48)
        tablero.append(self.button51)
        tablero.append(self.button52)
        tablero.append(self.button53)
        tablero.append(self.button54)
        tablero.append(self.button55)
        tablero.append(self.button56)
        tablero.append(self.button57)
        tablero.append(self.button58)
        tablero.append(self.button61)
        tablero.append(self.button62)
        tablero.append(self.button63)
        tablero.append(self.button64)
        tablero.append(self.button65)
        tablero.append(self.button66)
        tablero.append(self.button67)
        tablero.append(self.button68)
        tablero.append(self.button71)
        tablero.append(self.button72)
        tablero.append(self.button73)
        tablero.append(self.button74)
        tablero.append(self.button75)
        tablero.append(self.button76)
        tablero.append(self.button77)
        tablero.append(self.button78)
        tablero.append(self.button81)
        tablero.append(self.button82)
        tablero.append(self.button83)
        tablero.append(self.button84)
        tablero.append(self.button85)
        tablero.append(self.button86)
        tablero.append(self.button87)
        tablero.append(self.button88)


    def crearFichasNegras(self):
        negras.append(self.button12)
        negras.append(self.button14)
        negras.append(self.button16)
        negras.append(self.button18)
        negras.append(self.button21)
        negras.append(self.button23)
        negras.append(self.button25)
        negras.append(self.button27)
        negras.append(self.button32)
        negras.append(self.button34)
        negras.append(self.button36)
        negras.append(self.button38)
        for button in negras:
            button.setText('DamaNegra')

    def crearFichasBlancas(self):
        blancas.append(self.button61)
        blancas.append(self.button63)
        blancas.append(self.button65)
        blancas.append(self.button67)
        blancas.append(self.button72)
        blancas.append(self.button74)
        blancas.append(self.button76)
        blancas.append(self.button78)
        blancas.append(self.button81)
        blancas.append(self.button83)
        blancas.append(self.button85)
        blancas.append(self.button87)
        for button in blancas:
            button.setText('DamaBlanca')



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
