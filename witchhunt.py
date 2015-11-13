from random import randrange 

#from roles import Role 

players = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta']

#if 7 players, 2 have to be witches
witch1 = randrange(0,len(players))
print players[witch1]

if witch1 in players: 
    players_less = players.remove(witch1) 

witch2 = randrange(0,len(players_less))
print players_less[witch2]

#having global and local variable issues 


