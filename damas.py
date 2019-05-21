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
        negras.append(self.button54)
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

    def habilitarDeshabilitarBlancas(self):
        if self.miTurno == False:
            self.deshabilitarBotones()
            for button in blancas:
                button.setEnabled(True);
            self.miTurno=True;
        else:
            self.deshabilitarBotones();
            for button in negras:
                button.setEnabled(True);
            self.miTurno=False;
        print(self.sumaHeuristica(self.convertirTablero(arrayTablero)))

    def deshabilitarBotones(self):
        for button in tablero:
            button.setEnabled(False);
    def quitarColor(self):
        for bu in arrayTablero:
            for button in bu:
                if button.text()=="" or button.text()=="_":
                    button.setStyleSheet("background-color:light")
                    button.setText("")
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
                diagonales.append(arrayTablero[x-1][y+1].text())
        return diagonales;


    def mirarDiagonalNegras(self,x,y):
        diagonales=[];
        if (x+1)>7:
            diagonales.append("Fuera")
            diagonales.append("Fuera")
        else:
            if (y-1)<0:
                diagonales.append("Fuera");
            else:
                diagonales.append(arrayTablero[x+1][y-1].text())
            if (y+1)>7:
                diagonales.append("Fuera");
            else:
                diagonales.append(arrayTablero[x+1][y+1].text())
        return diagonales;

    def posibleMovimiento(self,b):
        botones=[];
        botones=self.buscarBoton(b);
        x=botones[0]
        y=botones[1]
        if b.text() == "DamaBlanca":
            self.posibleMovimientoX=x
            self.posibleMovimientoY=y
            movi=self.movimientosPeon(x-1,y-1,False,0)
            print (movi);
            if movi == 0:
                self.comer=False;
                self.siguienteMovimiento(x-2, y-2)
                self.siguienteMovimiento(x-2, y)
            elif movi == -1:
                return -1
            elif movi ==10:
                self.moverFicha(x-1, y-1, x-3, y-3,True)
            elif movi == 1:
                self.moverFicha(x-1, y-1, x-2, y-2,False)
            elif movi == 2:
                self.moverFicha(x-1, y-1, x-2, y,False)
            elif movi ==11:
                self.moverFicha(x-1, y-1, x-3, y+1,True)
            elif movi == 12:
                self.moverFicha(x-1, y-1, x-3, y+1,True)
            elif movi == 13:
                self.moverFicha(x-1, y-1, x-3, y-3,True)
            elif movi == 14:
                self.comer=True;
                self.siguienteMovimiento(x-3,y+1)
                self.siguienteMovimiento(x-3,y-3)
        elif b.text()=="DamaNegra":
            self.posibleMovimientoX=x
            self.posibleMovimientoY=y
            print(str(x) + str(y) +"pri")
            movi=self.movimientosPeonNegras(x-1,y-1)
            print (movi);
            if movi == 0:
                self.comer=False;
                self.siguienteMovimiento(x, y-2)
                self.siguienteMovimiento(x, y)
            elif movi == -1:
                return -1
            elif movi == 10:
                self.moverFichaNegras(x-1, y-1, x+1, y-3,True)
            elif movi == 1:
                self.moverFichaNegras(x-1, y-1, x, y-2,False)
            elif movi == 2:
                self.moverFichaNegras(x-1, y-1, x, y,False)
            elif movi == 11:
                self.moverFichaNegras(x-1, y-1, x, y+1,True)
            elif movi == 12:
                self.moverFichaNegras(x-1, y-1, x+1, y+1,True)
            elif movi == 13:
                self.moverFichaNegras(x-1, y-1, x+1, y-3,True)
            elif movi == 14:
                self.comer=True;
                self.siguienteMovimiento(x+1,y+1)
                self.siguienteMovimiento(x+1,y-3)
        elif b.text() == "_":
            if self.miTurno:
                if self.comer:
                    self.moverFicha(self.posibleMovimientoX-1,self.posibleMovimientoY-1,x-1,y-1,True)
                else:
                    self.moverFicha(self.posibleMovimientoX-1,self.posibleMovimientoY-1,x-1,y-1,False)
            else:
                if self.comer:
                    self.moverFichaNegras(self.posibleMovimientoX-1,self.posibleMovimientoY-1,x-1,y-1,True)
                else:
                    self.moverFichaNegras(self.posibleMovimientoX-1,self.posibleMovimientoY-1,x-1,y-1,False)


    def movimientosPeon(self,x,y):
        diagonales = self.mirarDiagonal(x,y)
        if diagonales[0]=="" and diagonales[1]=="":
            return 0
        elif diagonales[0]=="DamaBlanca" and diagonales[1]=="DamaBlanca":
            return -1
        elif diagonales[0]!="DamaBlanca" and (diagonales[1]=="DamaBlanca" or diagonales[1]=="Fuera"):
            if diagonales[0]=="DamaNegra":
                nuevaDiagonal=[]
                nuevaDiagonal = self.mirarDiagonal(x-1,y-1)
                if nuevaDiagonal[0] == "":
                    return 10
                elif nuevaDiagonal[0] != "":
                    return -1
            elif diagonales[0]=="":
                return 1
        elif (diagonales[0]=="DamaBlanca" or diagonales[0]=="Fuera") and diagonales[1]!="DamaBlanca":
            if diagonales[1]=="DamaNegra":
                nuevaDiagonal=[]
                nuevaDiagonal = self.mirarDiagonal(x-1,y+1)
                if nuevaDiagonal[1]=="":
                    return 11
                elif nuevaDiagonal[1]!="":
                    return -1
            elif diagonales[1]=="":
                return 2
        elif diagonales[0]!="DamaNegra" and diagonales[1]=="DamaNegra":
            if diagonales[0]=="DamaBlanca":
                nuevaDiagonal=[]
                nuevaDiagonal = self.mirarDiagonal(x-1,y+1)
                if nuevaDiagonal[1] == "":
                    return 12
                elif nuevaDiagonal[1] != "":
                    return -1
            elif diagonales[0]=="":
                nuevaDiagonal=[]
                nuevaDiagonal = self.mirarDiagonal(x-1,y+1)
                if nuevaDiagonal[1] == "":
                    return 12
                elif nuevaDiagonal[1] != "":
                    return 1
        elif diagonales[0]=="DamaNegra" and diagonales[1]!="DamaNegra":
            if diagonales[1]!="DamaBlanca":
                nuevaDiagonal=[]
                nuevaDiagonal = self.mirarDiagonal(x-1,y-1)
                if nuevaDiagonal[0] == "":
                    return 13
                elif nuevaDiagonal[0] != "":
                    return -1
            elif diagonales[1]=="":
                nuevaDiagonal=[]
                nuevaDiagonal = self.mirarDiagonal(x-1,y+1)
                if nuevaDiagonal[0] == "":
                    return 13
                elif nuevaDiagonal[0] != "":
                    return 2
        elif diagonales[0]=="DamaNegra" and diagonales[1]=="DamaNegra":
            diagonalIzquierda=[]
            diagonalDerecha=[]
            diagonalIzquierda=self.mirarDiagonal(x-1,y-1);
            diagonalDerecha=self.mirarDiagonal(x-1,y+1);
            if diagonalIzquierda[0]=="" and diagonalDerecha[1]=="":
                return 14 #Puede comer a los dos lados
            elif diagonalIzquierda[0]=="":
                return 13 #Solo puede comer a la izquierda
            elif diagonalDerecha[1]=="":
                return 12 #Solo puede comer a la derecha
            return -1 #No puede hacer nada

        return -2

    def movimientosPeonNegras(self,x,y):
        diagonales = self.mirarDiagonalNegras(x,y)
        print(str(x) + str(y));
        if diagonales[0]=="" and diagonales[1]=="":
            return 0 #PUEDE AVANZAR EN LAS DOS DIRECCIONES
        elif diagonales[0]=="DamaBlanca" and diagonales[1]=="DamaBlanca":
            diagonalIzquierda=self.mirarDiagonalNegras(x+1,y-1);
            diagonalDerecha=self.mirarDiagonalNegras(x+1,y+1);
            print(diagonalIzquierda[0] + diagonalIzquierda[1]+ str(x) + str(y))
            if diagonalIzquierda[0]=="" and diagonalDerecha[1]=="":
                return 14
            elif diagonalIzquierda[0]=="":
                return 13
            elif diagonalDerecha[1]=="":
                return 12
            return -1
        elif diagonales[0]!="DamaNegra" and (diagonales[1]=="DamaNegra" or diagonales[1]=="Fuera"):
            if diagonales[0]=="DamaBlanca":
                nuevaDiagonal = self.mirarDiagonalNegras(x+1, y-1)
                if nuevaDiagonal[0] == "":
                    return 10
                elif nuevaDiagonal[0] != "":
                    return -1
            elif diagonales[0]=="":
                return 1
        elif (diagonales[0]=="DamaNegra" or diagonales[0]=="Fuera") and diagonales[1]!="DamaNegra":
            if diagonales[1]=="DamaBlanca":
                nuevaDiagonal=self.mirarDiagonalNegras(x+1, y+1)
                if nuevaDiagonal[1]=="":
                    return 11
                elif nuevaDiagonal[1]!="":
                    return -1
            elif diagonales[1]=="":
                return 2
        elif diagonales[0]!="DamaBlanca" and diagonales[1]=="DamaBlanca":
            if diagonales[0]=="DamaNegra":
                nuevaDiagonal = self.mirarDiagonalNegras(x+1, y+1)
                if nuevaDiagonal[1] == "":
                    return 12
                elif nuevaDiagonal[1] != "":
                    return -1
            elif diagonales[0]=="":
                nuevaDiagonal = self.mirarDiagonalNegras(x+1, y+1)
                print("entro")
                if nuevaDiagonal[0] == "":
                    return 12
                elif nuevaDiagonal[0] != "":
                    return 1
        elif diagonales[0]=="DamaBlanca" and diagonales[1]!="DamaBlanca":
            if diagonales[1]!="DamaNegra":
                nuevaDiagonal = self.mirarDiagonalNegras(x+1, y-1)
                if nuevaDiagonal[1] == "":
                    return 13
                elif nuevaDiagonal[1] != "":
                    return -1
            elif diagonales[1]=="":
                nuevaDiagonal = self.mirarDiagonalNegras(x+1, y-1)
                if nuevaDiagonal[0] == "":
                    return 13
                elif nuevaDiagonal[0] != "":
                    return 2
        elif diagonales[0]=="DamaNegra" and diagonales[1]=="DamaNegra":
            return -1

        return -2

    def moverFicha(self,posX, posY, newX, newY,comer):
        print("1" + str(posX) + " 2" + str(posY))
        arrayTablero[posX][posY].setText("")
        arrayTablero[posX][posY].setEnabled(False)
        arrayTablero[newX][newY].setEnabled(True)
        arrayTablero[newX][newY].setText("DamaBlanca")
        arrayTablero[newX][newY].setStyleSheet("background-color:light")
        cont=0;
        for button in negras:
            if button.objectName() == arrayTablero[posX-1][posY-1].objectName():
                del negras[cont]
                print("a")
            cont = cont +1;
        cont=0
        blancas.append(arrayTablero[newX][newY])
        if comer:
            if(posY-newY)<0:
                arrayTablero[posX-1][posY+1].setText("")
            elif(posY-newY)>0:
                arrayTablero[posX-1][posY-1].setText("")
        self.quitarColor()

    def moverFichaNegras(self,posX, posY, newX, newY,comer):
        print("1-" + str(posX) + " 2-" + str(posY))
        arrayTablero[posX][posY].setText("")
        arrayTablero[posX][posY].setEnabled(False)
        arrayTablero[newX][newY].setEnabled(True)
        arrayTablero[newX][newY].setText("DamaNegra")
        arrayTablero[newX][newY].setStyleSheet("background-color:light")
        cont=0
        for button in blancas:
            if button.objectName() == arrayTablero[posX-1][posY-1].objectName():

                del blancas[cont]
            cont = cont +1;
        cont=0;
        negras.append(arrayTablero[newX-1][newY-1])
        if comer:
            if(posY-newY)>0:
                arrayTablero[posX+1][posY-1].setText("")
            elif(posY-newY)<0:
                arrayTablero[posX+1][posY+1].setText("")
        self.quitarColor()


    def siguienteMovimiento(self, x, y):
        arrayTablero[x][y].setEnabled(True)
        arrayTablero[x][y].setStyleSheet("background-color:green")
        arrayTablero[x][y].setText("_")

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

    def convertirTablero(self,tableroConvertir):
        tableroMinMax=[0] * n
        for i in range(n):
            tableroMinMax[i] = [0] * m
        x=0
        y=0
        for bu in tableroConvertir:
            for button in bu:
                if button.text() == "DamaBlanca":
                    tableroMinMax[x][y]=1;
                elif button.text() == "DamaNegra":
                    tableroMinMax[x][y]=-1;
                else:
                    tableroMinMax[x][y]=0;
                y=y+1
            y=0
            x=x+1
        return tableroMinMax

    def sumaHeuristica(self,tableroPuntuar):
        suma=0;
        for bu in tableroPuntuar:
            for ficha in bu:
                suma=suma+ficha
        return suma;

    def posiblesMovimientos(self, tableroMovimientos):
        movimientos=[]
        if self.turnoBlancas:
            for fila in tableroMovimientos:
                for columna in fila:
                    self.movimientosPeon(fila,columna,True,tableroMovimientos)




    def mirarDiagonalBlancasMinMax(self,x,y,tableroDiagonal):
        diagonales=[];
        if (x-1)<0:
            diagonales.append(10)
            diagonales.append(10)
        else:
            if (y-1)<0:
                diagonales.append(10);
            else:
                diagonales.append(tableroDiagonal[x-1][y-1])
            if (y+1)>7:
                diagonales.append(10);
            else:
                diagonales.append(tableroDiagonal[x-1][y+1])
        return diagonales;

    def mirarDiagonalNegrasMinMax(self,x,y,tableroDiagonal):
        diagonales=[];
        if (x+1)>7:
            diagonales.append(10)
            diagonales.append(10)
        else:
            if (y-1)<0:
                diagonales.append(10);
            else:
                diagonales.append(tableroDiagonal[x+1][y-1])
            if (y+1)>7:
                diagonales.append(10);
            else:
                diagonales.append(tableroDiagonal[x+1][y+1])
        return diagonales;
    
    def movimientoPeonBlancasMinMax(self,x,y,tableroPeonBlancasMinMax):
        diagonales = self.mirarDiagonalBlancasMinMax(x,y,tableroPeonBlancasMinMax)
        if diagonales[0]==0 and diagonales[1]==0:
            return 0
        elif diagonales[0]==1 and diagonales[1]==1:
            return -1
        elif diagonales[0]!=1 and (diagonales[1]==1 or diagonales[1]==10):
            if diagonales[0]==-1:
                nuevaDiagonal=[]
                nuevaDiagonal = self.mirarDiagonalBlancasMinMax(x-1,y-1,tableroPeonBlancasMinMax)
                if nuevaDiagonal[0] == 0:
                    return 10
                elif nuevaDiagonal[0] != 0:
                    return -1
            elif diagonales[0]==0:
                return 1
        elif (diagonales[0]==1 or diagonales[0]==10) and diagonales[1]!=1:
            if diagonales[1]==-1:
                nuevaDiagonal=[]
                nuevaDiagonal = self.mirarDiagonalBlancasMinMax(x-1,y+1,tableroPeonBlancasMinMax)
                if nuevaDiagonal[1]==0:
                    return 11
                elif nuevaDiagonal[1]!=0:
                    return -1
            elif diagonales[1]==0:
                return 2
        elif diagonales[0]!=-1 and diagonales[1]==-1:
            if diagonales[0]==1:
                nuevaDiagonal=[]
                nuevaDiagonal = self.mirarDiagonalBlancasMinMax(x-1,y+1,tableroPeonBlancasMinMax)
                if nuevaDiagonal[1] == 0:
                    return 12
                elif nuevaDiagonal[1] != 0:
                    return -1
            elif diagonales[0]==0:
                nuevaDiagonal=[]
                nuevaDiagonal = self.mirarDiagonalBlancasMinMax(x-1,y+1,tableroPeonBlancasMinMax)
                if nuevaDiagonal[1] == 0:
                    return 12
                elif nuevaDiagonal[1] != 0:
                    return 1
        elif diagonales[0]==-1 and diagonales[1]!=-1:
            if diagonales[1]!=1:
                nuevaDiagonal=[]
                nuevaDiagonal = self.mirarDiagonalBlancasMinMax(x-1,y-1,tableroPeonBlancasMinMax)
                if nuevaDiagonal[0] == 0:
                    return 13
                elif nuevaDiagonal[0] != 0:
                    return -1
            elif diagonales[1]==0:
                nuevaDiagonal=[]
                nuevaDiagonal = self.mirarDiagonalBlancasMinMax(x-1,y+1,tableroPeonBlancasMinMax)
                if nuevaDiagonal[0] == 0:
                    return 13
                elif nuevaDiagonal[0] != 0:
                    return 2
        elif diagonales[0]==-1 and diagonales[1]==-1:
            diagonalIzquierda=[]
            diagonalDerecha=[]
            diagonalIzquierda=self.mirarDiagonalBlancasMinMax(x-1,y-1,tableroPeonBlancasMinMax);
            diagonalDerecha=self.mirarDiagonalBlancasMinMax(x-1,y+1,tableroPeonBlancasMinMax);
            if diagonalIzquierda[0]==0 and diagonalDerecha[1]==0:
                return 14 #Puede comer a los dos lados
            elif diagonalIzquierda[0]==0:
                return 13 #Solo puede comer a la izquierda
            elif diagonalDerecha[1]==0:
                return 12 #Solo puede comer a la derecha
            return -1 #No puede hacer nada

    def movimientosPeonNegrasMinMax(self,x,y,tableroPeonNegrasMinMax):
        diagonales = self.mirarDiagonalNegrasMinMax(x,y,tableroPeonNegrasMinMax)
        print(str(x) + str(y));
        if diagonales[0]==0 and diagonales[1]==0:
            return 0 #PUEDE AVANZAR EN LAS DOS DIRECCIONES
        elif diagonales[0]==1 and diagonales[1]==1:
            diagonalIzquierda=self.mirarDiagonalNegrasMinMax(x+1,y-1,tableroPeonNegrasMinMax);
            diagonalDerecha=self.mirarDiagonalNegrasMinMax(x+1,y+1,tableroPeonNegrasMinMax);
            print(diagonalIzquierda[0] + diagonalIzquierda[1]+ str(x) + str(y))
            if diagonalIzquierda[0]==0 and diagonalDerecha[1]==0:
                return 14
            elif diagonalIzquierda[0]==0:
                return 13
            elif diagonalDerecha[1]==0:
                return 12
            return -1
        elif diagonales[0]!=-1 and (diagonales[1]==-1 or diagonales[1]==10):
            if diagonales[0]==1:
                nuevaDiagonal = self.mirarDiagonalNegrasMinMax(x+1, y-1,tableroPeonNegrasMinMax)
                if nuevaDiagonal[0] == 1:
                    return 10
                elif nuevaDiagonal[0] != 1:
                    return -1
            elif diagonales[0]==0:
                return 1
        elif (diagonales[0]==-1 or diagonales[0]==10) and diagonales[1]!=-1:
            if diagonales[1]==1:
                nuevaDiagonal=self.mirarDiagonalNegrasMinMax(x+1, y+1,tableroPeonNegrasMinMax)
                if nuevaDiagonal[1]==0:
                    return 11
                elif nuevaDiagonal[1]!=0:
                    return -1
            elif diagonales[1]==0:
                return 2
        elif diagonales[0]!=1 and diagonales[1]==1:
            if diagonales[0]==-1:
                nuevaDiagonal = self.mirarDiagonalNegrasMinMax(x+1, y+1,tableroPeonNegrasMinMax)
                if nuevaDiagonal[1] == 0:
                    return 12
                elif nuevaDiagonal[1] != 0:
                    return -1
            elif diagonales[0]==0:
                nuevaDiagonal = self.mirarDiagonalNegrasMinMax(x+1, y+1,tableroPeonNegrasMinMax)
                print("entro")
                if nuevaDiagonal[0] == 0:
                    return 12
                elif nuevaDiagonal[0] != 0:
                    return 1
        elif diagonales[0]==1 and diagonales[1]!=1:
            if diagonales[1]!=-1:
                nuevaDiagonal = self.mirarDiagonalNegrasMinMax(x+1, y-1,tableroPeonNegrasMinMax)
                if nuevaDiagonal[1] == 0:
                    return 13
                elif nuevaDiagonal[1] != 0:
                    return -1
            elif diagonales[1]==0:
                nuevaDiagonal = self.mirarDiagonalNegrasMinMax(x+1, y-1,tableroPeonNegrasMinMax)
                if nuevaDiagonal[0] == 0:
                    return 13
                elif nuevaDiagonal[0] != 0:
                    return 2
        elif diagonales[0]==-1 and diagonales[1]==-1:
            return -1

        return -2
    
    def todosMovimientosBlancas(self,tableroTodos):
        movimientos=[]
        for filas in tableroTodos:
            for columnas in filas:
                if columnas == 1:
                    self.movimientoPeonBlancasMinMax(filas,columnas,tableroTodos)
                    
    def todosMovimientosNegras(self,tableroTodos):
        movimientos=[]
        for filas in tableroTodos:
            for columnas in filas:
                if columnas == -1:
                    self.movimientosPeonNegrasMinMax(filas,columnas,tableroTodos)
                    
    def minMax(self,tableroMinMax,profundidad,turno)
        tableros=[]
        
        if turno=="Blancas":
            tableros=self.todosMovimientosBlancas(tableroMinMax)
            for tablero in tableros:
                Max(self.minMax(tablero,profundidad-1,Negras))
        elif turno == "Negras":
            tableros=self.todosMovimientosNegras(tableroMinMax)
            for tablero in tableros:
                Min(self.minMax(tablero,profundidad-1,Blancas))
            
            

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
