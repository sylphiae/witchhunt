from random import randrange 
import random 
import roles 


player_roles = [roles.priest1, roles.apprentice1, roles.judge1, roles.gravedigger1, roles.survivalist1, roles.dob1, roles.gambler1]
players = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta']
random.shuffle(players)
initial_game = {}
n = 0 
for player in players: 
		print player 
		initial_game[player] = player_roles[n]
		n = n + 1 

print initial_game 

witches = [] 
villagers = []

for player, role in initial_game.iteritems():
	#print player 
	#print id(role)
	if role == roles.priest1:
		print player
		villager1 = player

print villager1 



#witches = random.sample(players, 2)
#print witches 

#for player in players: 
#	if player in witches: 
		

'''need to check if priest is a witch, if so need to pick a new witch-
priest is alpha)'''

#for witch in witches: 
#	if witch == 'alpha': 
#		random.sample(players)



#if 7 players, 2 have to be witches
#witch1 = randrange(0,len(players))
#print players[witch1]

#if witch1 in players: 
 #   players_less = players.remove(witch1) 

#witch2 = randrange(0,len(players_less))
#print players_less[witch2]

#having global and local variable issues 





