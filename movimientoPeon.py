def movimientosPeonBlancas(self,x,y):
        diagonales = self.mirarDiagonalBlancas(x,y)
        if diagonales[0]=="" and diagonales[1]=="": #BOTH SIDES ARE FREE
            return 0
		elif diagonales[0]=="" and diagonales[1]!="": #LEFT CELL IS FREE
			return 1
		elif diagonales[0]!="" and diagonales[1]=="": #RIGHT CELL IS FREE
			return 2
		elif diagonales[0]=="white" and diagonales[1]=="white": #BOTH SIDES ARE FULL, SAME PIECE
			return -1
		elif diagonales[0]=="black" and diagonales[1]=="white": #BOTH FULL, MAY EAT ON LEFT
			nuevaDiagonal=[]
			nuevaDiagonal=self.mirarDiagonalBlancas(x-1, y-1)
			if nuevaDiagonal[0]=="":
				return 3
			elif nuevaDiagonal[0]!="":
				return -1
			return -5 #CHECK ERROR
		elif diagonales[0]=="white" and diagonales[1]=="black": #BOTH FULL, MAY EAT ON RIGHT
			nuevaDiagonal=[]
			nuevaDiagonal=self.mirarDiagonalBlancas(x-1, y+1)
			if nuevaDiagonal[1]=="":
				return 4
			elif nuevaDiagonal[1]!="":
				return -1
			return -5 #CHECK ERROR
        elif diagonales[0]=="black" and diagonales[1]=="black": #BOTH FULL, MAY EAT ON BOTH
			nuevaDiagonalIzq=[]
			nuevaDiagonalDch=[]
			nuevaDiagonalIzq=self.mirarDiagonalBlancas(x-1,y-1)
			nuevaDiagonalDch=self.mirarDiagonalBlancas(x-1,y+1)
			if diagonalIzquierda[0]=="" and diagonalDerecha[1]=="":
				return 5
			elif diagonalIzquierda[0]=="" and diagonalDerecha[1]!="":
				return 3
			elif diagonalIzquierda[0]!="" and diagonalDerecha[1]=="":
				return 4
			elif diagonalIzquierda[0]!="" and diagonalDerecha[1]!="":
				return -1				
		return -2 #IF-ELSE ERROR
