#main method to invoke classes 
#attribute turn day or night
#type coercion 

class Role(object):
    
    def _init_(self, name, alignment, is_awake, is_dead, ability):
        self.name = name
        self.alignment = alignment
        self.is_awake = is_awake 
        self.is_dead = is_dead
        self.ability = ability

    def getName(self):
        return self.name 

    def getAbility(self):
    	return self.ability 

class Priest(Role):
   #	__instance = None
    #def __new__(self, name, alignment, is_awake, is_dead, ability):
        #if Priest.__instance is None:
        	#Priest.__instance = object.__new__(self, name, alignment, is_awake, is_dead, ability)
        #Priest.__instance.val = val
        #return Priest.__instance
	

	def whois(self):
		return self.whois 

priest1 = Priest()


class Apprentice(Role):

	def choice(self):
		return self.choice

apprentice1 = Apprentice()

class Judge(Role):
	

	def kill_choice(self):
		return self.kill_choice

judge1 = Judge()

class Gravedigger(Role):


	def whois(self):
		return self.whois 

gravedigger1 = Gravedigger()


class Survivalist(Role):
	

	def lives_left(self):
		return self.lives_left

survivalist1 = Survivalist()

class DOB(Role):

	def kill_with(self):
		return self.kill_with

dob1 = DOB()

class Gambler(Role):
	

	def even_odd(self):
		return self.even_odd

gambler1 = Gambler()

class Angel(Role):
	

	def pick(self):
		return self.pick

class Demon(Role):
	
	def pick(self):
		return self.pick


