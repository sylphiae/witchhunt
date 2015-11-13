class Role(object):
    
    def _init_(self, name, alignment, is_awake, is_dead, ability)
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
	def __init__(self, name, alignment, is_awake, is_dead, ability):
		Role.__init__(self, name, alignment, is_awake, is_dead, ability)
		self.whois = whois

	def whois(self):
		return self.whois 


class Apprentice(Role):
	def __init__(self, name, alignment, is_awake, is_dead, ability):
		Role.__init__(self, name, alignment, is_awake, is_dead, ability)
		self.choice = choice

	def choice(self):
		return self.choice


class Judge(Role):
	def __init__(self, name, alignment, is_awake, is_dead, ability):
		Role.__init__(self, name, alignment, is_awake, is_dead, ability)
		self.kill_choice = kill_choice

	def kill_choice(self):
		return self.kill_choice


class Gravedigger(Role):
	def __init__(self, name, alignment, is_awake, is_dead, ability):
		Role.__init__(self, name, alignment, is_awake, is_dead, ability)
		self.whois = whois

	def whois(self):
		return self.whois 


class Survivalist(Role):
	def __init__(self, name, alignment, is_awake, is_dead, ability):
		Role.__init__(self, name, alignment, is_awake, is_dead, ability)
		self.lives_left = lives_left

	def lives_left(self):
		return self.lives_left


class DOB(Role):
	def __init__(self, name, alignment, is_awake, is_dead, ability):
		Role.__init__(self, name, alignment, is_awake, is_dead, ability)
		self.kill_with = kill_with

	def kill_with(self):
		return self.kill_with



class Gambler(Role):
	def __init__(self, name, alignment, is_awake, is_dead, ability):
		Role.__init__(self, name, alignment, is_awake, is_dead, ability)
		self.even_odd = even_odd

	def even_odd(self):
		return self.even_odd

class Angel(Role):
	def __init__(self, name, alignment, is_awake, is_dead, ability):
		Role.__init__(self, name, alignment, is_awake, is_dead, ability)
		self.pick = pick

	def pick(self):
		return self.pick

class Demon(Role):
	def __init__(self, name, alignment, is_awake, is_dead, ability):
		Role.__init__(self, name, alignment, is_awake, is_dead, ability)
		self.pick = pick

	def pick(self):
		return self.pick


