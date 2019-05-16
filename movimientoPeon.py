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
				nuevaDiagonal=self.mirarDiagonal(x-1, y-1)
				if nuevaDiagonal[0]==""
					#PUEDO COMER...LLAMO A comerFicha, LLAMO A moverFicha					
					#LLAMO A movimientosPeon
				elif nuevaDiagonal[0]!=""
					return -1	
			elif diagonales[0]=="": #PUEDE AVANZAR A LA IZDA
				return 1		
		elif diagonales[0]=="DamaBlanca" and diagonales[1]!="DamaBlanca": #NO PUEDE MOVERSE POR LA IZDA, PERO QUIZA PUEDA COMER O AVANZAR POR LA DCHA	
			if diagonales[1]=="DamaNegra": #ENEMIGO AL LADO, MIRAR SIGUIENTE POSICIÓN
			#SI VACIO COMER Y MIRAR SIGUIENTE POSICIÓN, SI FUERA NO MOVER, SI NO VACIO NO MOVER
			#FOREACH AQUI HASTA QUE RETORNE -1 CON UN CONTADOR QUE VAYA MIRANDO 
				nuevaDiagonal=self.mirarDiagonal(x-1, y+1)
				if nuevaDiagonal[1]==""
					#PUEDO COMER...LLAMO A comerFicha, LLAMO A moverFicha					
					#LLAMO A movimientosPeon
				elif nuevaDiagonal[1]!=""
					return -1	
			elif diagonales[1]=="": #PUEDE AVANZAR A LA DCHA
				return 2
			
		return -2 #FALLO EN IF-ELSEs
	
	
def comerFicha(posX, posY, newX, newY)				
		arrayTablero[posX, posY].setText("")
		arrayTablero[newX, newY].setText("DamaBlanca")
		arrayTablero[posX-(posX-newX), posY-(posY-newY)].setText("")
		cont=1
		for boton in negras:
			if boton.objectName()==arrayTablero[posX-(posX-newX), posY-(posY-newY)].objectName():
				negras.remove(cont)
			cont++
