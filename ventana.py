from ventana_ui import *

tablero = [];
negras = [];
blancas = [];
n = 8
m = 8
arrayTablero = [0] * n
for i in range(n):
    arrayTablero[i] = [0] * m


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.miTurno=False;
        self.setupUi(self)
        self.crearArraysTablero();
        self.crearFichasNegras();
        self.crearFichasBlancas();
        self.deshabilitarBotones();
        self.crearArrayBiDimensional();
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

    def mirarDiagonal(self,x,y):
        diagonales=[];
        if (x-1)<0:
            diagonales.append("Fuera")
            diagonales.append("Fuera")
        else:
            if (y-1)<0:
                diagonales.append("Fuera");
            else:
                diagonales.append(arrayTablero[x-1][y-1].text())
            if (y+1)>7:
                diagonales.append("Fuera");
            else:
                diagonales.append(arrayTablero[x-1][y-1].text())
        return diagonales;


    def actualizar(self):
        self.button33.setText("¡Acabas de hacer clic en el botón!")

    def crearArrayBiDimensional(self):
        arrayTablero[0][0]=self.button11
        arrayTablero[0][1]=self.button12
        arrayTablero[0][2]=self.button13
        arrayTablero[0][3]=self.button14
        arrayTablero[0][4]=self.button15
        arrayTablero[0][5]=self.button16
        arrayTablero[0][6]=self.button17
        arrayTablero[0][7]=self.button18
        arrayTablero[1][0]=self.button21
        arrayTablero[1][1]=self.button22
        arrayTablero[1][2]=self.button23
        arrayTablero[1][3]=self.button24
        arrayTablero[1][4]=self.button25
        arrayTablero[1][5]=self.button26
        arrayTablero[1][6]=self.button27
        arrayTablero[1][7]=self.button28
        arrayTablero[2][0]=self.button31
        arrayTablero[2][1]=self.button32
        arrayTablero[2][2]=self.button33
        arrayTablero[2][3]=self.button34
        arrayTablero[2][4]=self.button35
        arrayTablero[2][5]=self.button36
        arrayTablero[2][6]=self.button37
        arrayTablero[2][7]=self.button38
        arrayTablero[3][0]=self.button41
        arrayTablero[3][1]=self.button42
        arrayTablero[3][2]=self.button43
        arrayTablero[3][3]=self.button44
        arrayTablero[3][4]=self.button45
        arrayTablero[3][5]=self.button46
        arrayTablero[3][6]=self.button47
        arrayTablero[3][7]=self.button48
        arrayTablero[4][0]=self.button51
        arrayTablero[4][1]=self.button52
        arrayTablero[4][2]=self.button53
        arrayTablero[4][3]=self.button54
        arrayTablero[4][4]=self.button55
        arrayTablero[4][5]=self.button56
        arrayTablero[4][6]=self.button57
        arrayTablero[4][7]=self.button58
        arrayTablero[5][0]=self.button61
        arrayTablero[5][1]=self.button62
        arrayTablero[5][2]=self.button63
        arrayTablero[5][3]=self.button64
        arrayTablero[5][4]=self.button65
        arrayTablero[5][5]=self.button66
        arrayTablero[5][6]=self.button67
        arrayTablero[5][7]=self.button68
        arrayTablero[6][0]=self.button71
        arrayTablero[6][1]=self.button72
        arrayTablero[6][2]=self.button73
        arrayTablero[6][3]=self.button74
        arrayTablero[6][4]=self.button75
        arrayTablero[6][5]=self.button76
        arrayTablero[6][6]=self.button77
        arrayTablero[6][7]=self.button78
        arrayTablero[7][0]=self.button81
        arrayTablero[7][1]=self.button82
        arrayTablero[7][2]=self.button83
        arrayTablero[7][3]=self.button84
        arrayTablero[7][4]=self.button85
        arrayTablero[7][5]=self.button86
        arrayTablero[7][6]=self.button87
        arrayTablero[7][7]=self.button88


    def crearArraysTablero(self):
        tablero.append(self.button11)
        self.button11.clicked.connect(lambda: self.posibleMovimiento(self.button11));
        tablero.append(self.button12)
        self.button12.clicked.connect(lambda: self.posibleMovimiento(self.button12));
        tablero.append(self.button13)
        self.button13.clicked.connect(lambda: self.posibleMovimiento(self.button13));
        tablero.append(self.button14)
        self.button14.clicked.connect(lambda: self.posibleMovimiento(self.button14));
        tablero.append(self.button15)
        self.button15.clicked.connect(lambda: self.posibleMovimiento(self.button15));
        tablero.append(self.button16)
        self.button16.clicked.connect(lambda: self.posibleMovimiento(self.button16));
        tablero.append(self.button17)
        self.button17.clicked.connect(lambda: self.posibleMovimiento(self.button17));
        tablero.append(self.button18)
        self.button18.clicked.connect(lambda: self.posibleMovimiento(self.button18));
        tablero.append(self.button21)
        self.button21.clicked.connect(lambda: self.posibleMovimiento(self.button21));
        tablero.append(self.button22)
        self.button22.clicked.connect(lambda: self.posibleMovimiento(self.button22));
        tablero.append(self.button23)
        self.button23.clicked.connect(lambda: self.posibleMovimiento(self.button23));
        tablero.append(self.button24)
        self.button24.clicked.connect(lambda: self.posibleMovimiento(self.button24));
        tablero.append(self.button25)
        self.button25.clicked.connect(lambda: self.posibleMovimiento(self.button25));
        tablero.append(self.button26)
        self.button26.clicked.connect(lambda: self.posibleMovimiento(self.button26));
        tablero.append(self.button27)
        self.button27.clicked.connect(lambda: self.posibleMovimiento(self.button27));
        tablero.append(self.button28)
        self.button28.clicked.connect(lambda: self.posibleMovimiento(self.button28));
        tablero.append(self.button31)
        self.button31.clicked.connect(lambda: self.posibleMovimiento(self.button31));
        tablero.append(self.button32)
        self.button32.clicked.connect(lambda: self.posibleMovimiento(self.button32));
        tablero.append(self.button33)
        self.button33.clicked.connect(lambda: self.posibleMovimiento(self.button33));
        tablero.append(self.button34)
        self.button34.clicked.connect(lambda: self.posibleMovimiento(self.button34));
        tablero.append(self.button35)
        self.button35.clicked.connect(lambda: self.posibleMovimiento(self.button35));
        tablero.append(self.button36)
        self.button36.clicked.connect(lambda: self.posibleMovimiento(self.button36));
        tablero.append(self.button37)
        self.button37.clicked.connect(lambda: self.posibleMovimiento(self.button37));
        tablero.append(self.button38)
        self.button38.clicked.connect(lambda: self.posibleMovimiento(self.button38));
        tablero.append(self.button41)
        self.button41.clicked.connect(lambda: self.posibleMovimiento(self.button41));
        tablero.append(self.button42)
        self.button42.clicked.connect(lambda: self.posibleMovimiento(self.button42));
        tablero.append(self.button43)
        self.button43.clicked.connect(lambda: self.posibleMovimiento(self.button43));
        tablero.append(self.button44)
        self.button44.clicked.connect(lambda: self.posibleMovimiento(self.button44));
        tablero.append(self.button45)
        self.button45.clicked.connect(lambda: self.posibleMovimiento(self.button45));
        tablero.append(self.button46)
        self.button46.clicked.connect(lambda: self.posibleMovimiento(self.button46));
        tablero.append(self.button47)
        self.button47.clicked.connect(lambda: self.posibleMovimiento(self.button47));
        tablero.append(self.button48)
        self.button48.clicked.connect(lambda: self.posibleMovimiento(self.button48));
        tablero.append(self.button51)
        self.button51.clicked.connect(lambda: self.posibleMovimiento(self.button51));
        tablero.append(self.button52)
        self.button52.clicked.connect(lambda: self.posibleMovimiento(self.button52));
        tablero.append(self.button53)
        self.button53.clicked.connect(lambda: self.posibleMovimiento(self.button53));
        tablero.append(self.button54)
        self.button54.clicked.connect(lambda: self.posibleMovimiento(self.button54));
        tablero.append(self.button55)
        self.button55.clicked.connect(lambda: self.posibleMovimiento(self.button55));
        tablero.append(self.button56)
        self.button56.clicked.connect(lambda: self.posibleMovimiento(self.button56));
        tablero.append(self.button57)
        self.button57.clicked.connect(lambda: self.posibleMovimiento(self.button57));
        tablero.append(self.button58)
        self.button58.clicked.connect(lambda: self.posibleMovimiento(self.button58));
        tablero.append(self.button61)
        self.button61.clicked.connect(lambda: self.posibleMovimiento(self.button61));
        tablero.append(self.button62)
        self.button62.clicked.connect(lambda: self.posibleMovimiento(self.button62));
        tablero.append(self.button63)
        self.button63.clicked.connect(lambda: self.posibleMovimiento(self.button63));
        tablero.append(self.button64)
        self.button64.clicked.connect(lambda: self.posibleMovimiento(self.button64));
        tablero.append(self.button65)
        self.button65.clicked.connect(lambda: self.posibleMovimiento(self.button65));
        tablero.append(self.button66)
        self.button66.clicked.connect(lambda: self.posibleMovimiento(self.button66));
        tablero.append(self.button67)
        self.button67.clicked.connect(lambda: self.posibleMovimiento(self.button67));
        tablero.append(self.button68)
        self.button68.clicked.connect(lambda: self.posibleMovimiento(self.button68));
        tablero.append(self.button71)
        self.button71.clicked.connect(lambda: self.posibleMovimiento(self.button71));
        tablero.append(self.button72)
        self.button72.clicked.connect(lambda: self.posibleMovimiento(self.button72));
        tablero.append(self.button73)
        self.button73.clicked.connect(lambda: self.posibleMovimiento(self.button73));
        tablero.append(self.button74)
        self.button74.clicked.connect(lambda: self.posibleMovimiento(self.button74));
        tablero.append(self.button75)
        self.button75.clicked.connect(lambda: self.posibleMovimiento(self.button75));
        tablero.append(self.button76)
        self.button76.clicked.connect(lambda: self.posibleMovimiento(self.button76));
        tablero.append(self.button77)
        self.button77.clicked.connect(lambda: self.posibleMovimiento(self.button77));
        tablero.append(self.button78)
        self.button78.clicked.connect(lambda: self.posibleMovimiento(self.button78));
        tablero.append(self.button81)
        self.button81.clicked.connect(lambda: self.posibleMovimiento(self.button81));
        tablero.append(self.button82)
        self.button82.clicked.connect(lambda: self.posibleMovimiento(self.button82));
        tablero.append(self.button83)
        self.button83.clicked.connect(lambda: self.posibleMovimiento(self.button83));
        tablero.append(self.button84)
        self.button84.clicked.connect(lambda: self.posibleMovimiento(self.button84));
        tablero.append(self.button85)
        self.button85.clicked.connect(lambda: self.posibleMovimiento(self.button85));
        tablero.append(self.button86)
        self.button86.clicked.connect(lambda: self.posibleMovimiento(self.button86));
        tablero.append(self.button87)
        self.button87.clicked.connect(lambda: self.posibleMovimiento(self.button87));
        tablero.append(self.button88)
        self.button88.clicked.connect(lambda: self.posibleMovimiento(self.button88));


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


    def posibleMovimiento(self,b):
        botones=[];
        if b.text() == "DamaBlanca":
            botones=self.buscarBoton(b);
            x=botones[0]
            y=botones[1]
            movi=self.movimientosPeon(x-1,y-1)
            if movi == 0:
                #SE PUEDE MOVER A AMBOS LADOS, LAS HABILITAS PINTAS DE VERDE, Y SEGUN CUAL PULSE VAS A ELLA
                self.comerFicha(x-1,y-1,x-3,y-3)

    def movimientosPeon(self,x,y):
        diagonales = self.mirarDiagonal(x,y)
        if diagonales[0]=="" and diagonales[1]=="":
            return 0 #PUEDE AVANZAR EN LAS DOS DIRECCIONES
        elif diagonales[0]=="DamaBlanca" and diagonales[1]=="DamaBlanca":
            return -1 #NO PUEDE AVANZAR A NINGUNA POSICIÓN
        elif diagonales[0]!="DamaBlanca" and diagonales[1]=="DamaBlanca": #NO PUEDE MOVERSE POR LA DCHA, PERO QUIZA PUEDA COMER O AVANZAR POR LA IZDA
            if diagonales[0]=="DamaNegra": #ENEMIGO AL LADO, MIRAR SIGUIENTE POSICIÓN
			#SI VACIO COMER Y MIRAR SIGUIENTE POSICIÓN, SI FUERA NO MOVER, SI NO VACIO NO MOVER
			#FOREACH AQUI HASTA QUE RETORNE -1 CON UN CONTADOR QUE VAYA MIRANDO
                nuevaDiagonal = self.mirarDiagonal(x-1, y-1)
                if nuevaDiagonal[0] == "":
                    return 10
					#PUEDO COMER...LLAMO A comerFicha, LLAMO A moverFicha
					#LLAMO A movimientosPeon
                elif nuevaDiagonal[0] != "":
                    return -1
            elif diagonales[0]=="": #PUEDE AVANZAR A LA IZDA
                return 1
        elif diagonales[0]=="DamaBlanca" and diagonales[1]!="DamaBlanca": #NO PUEDE MOVERSE POR LA IZDA, PERO QUIZA PUEDA COMER O AVANZAR POR LA DCHA
            if diagonales[1]=="DamaNegra": #ENEMIGO AL LADO, MIRAR SIGUIENTE POSICIÓN
			#SI VACIO COMER Y MIRAR SIGUIENTE POSICIÓN, SI FUERA NO MOVER, SI NO VACIO NO MOVER
			#FOREACH AQUI HASTA QUE RETORNE -1 CON UN CONTADOR QUE VAYA MIRANDO
                nuevaDiagonal=self.mirarDiagonal(x-1, y+1)
                if nuevaDiagonal[1]=="":
                    return 11
					#PUEDO COMER...LLAMO A comerFicha, LLAMO A moverFicha
					#LLAMO A movimientosPeon
                elif nuevaDiagonal[1]!="":
                    return -1
            elif diagonales[1]=="": #PUEDE AVANZAR A LA DCHA
                return 2

        return -2 #FALLO EN IF-ELSEs

    def comerFicha(self,posX, posY, newX, newY):
        print(posX, posY, newX, newY)
        arrayTablero[posX][posY].setText("")
        arrayTablero[posX][posY].setEnabled(False)
        arrayTablero[newX][newY].setEnabled(True)
        arrayTablero[newX][newY].setText("DamaBlanca")
        arrayTablero[posX-1][posY-1].setText("")
        cont=1
        for boton in negras:
            if boton.objectName()==arrayTablero[posX-(posX-newX)][posY-(posY-newY)].objectName():
                negras.remove(cont)
            cont=cont+1

    def buscarBoton(self,b):
        x=1;
        y=1;
        button=[];
        for array in arrayTablero:
            for boton in array:
                if b.objectName() == boton.objectName():
                    button.append(x);
                    button.append(y);
                    button.append(b);
                y=y+1;
            y=1;
            x=x+1;
        return button;


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
