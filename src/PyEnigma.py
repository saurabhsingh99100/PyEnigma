class pyenigma:
	
	ROTOR_A = ['D','U','X','K','L','T','W','A','J','M','C','V','R','P','B','I','H','Z','G','O','N','E','Y','Q','F','S']
	ROTOR_B = ['X','R','E','J','D','W','Q','S','I','B','C','Y','V','O','T','A','L','H','U','N','M','F','Z','P','K','G']
	ROTOR_C = ['N','M','U','B','P','F','V','T','O','A','L','D','G','H','K','E','Q','X','I','S','C','Z','W','J','R','Y']
	
	def __init__(self, a=0, b=0, c=0):
		self.__Apos = a
		self.__Bpos = b
		self.__Cpos = c
	
		self.__rotorA = self.__offset(self.ROTOR_A, self.__Apos)
		self.__rotorB = self.__offset(self.ROTOR_B, self.__Bpos)
		self.__rotorC = self.__offset(self.ROTOR_C, self.__Cpos)
		return
		
			
	#-------------------------------------- API --------------------------------------------------------
	def currentSetting(self):
		return [self.__Apos, self.__Bpos, self.__Cpos]
	
	def changeSetting(self, a, b, c):
		self.__Apos = int(a)
		self.__Bpos = int(b)
		self.__Cpos = int(c)
	
		self.__rotorA = self.__offset(self.ROTOR_A, self.__Apos)
		self.__rotorB = self.__offset(self.ROTOR_B, self.__Bpos)
		self.__rotorC = self.__offset(self.ROTOR_C, self.__Cpos)
		return
	
	def reset(self): 
		#reset rotors to last setting
		self.resetZ() 													#reset to 0,0,0
		self.__rotorA = self.__offset(self.ROTOR_A, self.__Apos) 	# offset each by last setting
		self.__rotorB = self.__offset(self.ROTOR_B, self.__Bpos)
		self.__rotorC = self.__offset(self.ROTOR_C, self.__Cpos)
		return

	def resetZ(self):
		#reset rotors to 0,0,0
		self.__rotorA = self.ROTOR_A
		self.__rotorB = self.ROTOR_B
		self.__rotorC = self.ROTOR_C
		return

	def run(self, msg):
		msg = msg.upper()
		out = ""

		for l0 in msg:
			if l0 == " ":
				out+=" "
			else:
				l1 = self.__passForward(self.__rotorA, l0)
				l2 = self.__passForward(self.__rotorB, l1)
				l3 = self.__passForward(self.__rotorC, l2)
				l4 = self.__mirror(l3)
				l5 = self.__passBackward(self.__rotorC, l4)
				l6 = self.__passBackward(self.__rotorB, l5)
				l7 = self.__passBackward(self.__rotorA, l6)

				out+=l7

				self.__rotorA = self.__spin(self.__rotorA)
				self.__rotorB = self.__spin(self.__rotorB)
				self.__rotorC = self.__spin(self.__rotorC)
		
		return out
	
	#------------------------------------------------------------------------------------------------------	

	def __offset(self, rotor, num):
		# used to initialise a rotor by offsetting by certain amount
		if (num>=25 or num<0):
			print("!ERROR : offset out of range; \ndesired range : 0 <= offset <= 25")
		else:
			for i in range(0, num):
				rotor = self.__spin(rotor)
		return rotor
			 		
		
	def __spin(self, rotor):
		L = rotor[-1]
		rotor = rotor[0:25]
		rotor = [L]+rotor
		return rotor


	def __passForward(self, rotor, Letter):
		return rotor[ord(Letter)-65]


	def __passBackward(self, rotor, Letter):
		return chr(rotor.index(Letter)+65)


	def __mirror(self, Letter):
		i = (ord(Letter)-65)
		i = 25-i
		return chr(i+65)
	
