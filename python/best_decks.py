###program to create a ranking of my Hearthstone decks





########################################################################
### modules ###
########################################################################

'''
import modules and functions
'''

import pandas as pd
import parameters
from HSModule.HSDeck import HS_Deck




########################################################################
### parameters, data###
########################################################################

'''
Defines parameters and opens data 
'''

data_file 	= parameters.data_file 		#file name
factor		= parameters.factor			#factor for calculation of rating
data 		= pd.read_csv(data_file)	#open data file
ranking		= []						#will be filled with decks in ranked order





########################################################################
### Create Deck-Objectives ###
########################################################################

'''
Creates a Hearthstone_deck - objective for each Hearthstone deck.
'''

deck1 = HS_Deck('Lifecoach','Warrior','Dragon',1)
deck2 = HS_Deck('ThijsNL','Warlock','Reno',1)
deck3 = HS_Deck('ThijsNL','Priest','Dragon',1)
deck4 = HS_Deck('Lifecoach','Shaman','Jade',1)
deck5 = HS_Deck('ThijsNL','Warrior','Pirate',1)

decks = [deck1,deck2,deck3,deck4,deck5]





########################################################################
### read in data ###
########################################################################

'''
reads in deck specific data for each deck
'''

###read in deck specific data for each deck
for deck in decks:
	deck.read_file(data)	




	
########################################################################
### Ranking ###
########################################################################

'''
Calculates a rating for each deck. The rating is depending on the number
of games played with the deck. Thus, decks are only compared by 
calculating a rating of the last 'x' games, with 'x' beeing the minimum
number of games played with the decks. 
The worst deck is then excluded, and the same calculation done again,
with a new minimum number of games played, for the remaining decks.
This is repeated until there is no deck left to exclude.
'''

###calculate ranking for each deck with minimum number of games until there is no deck left
while len(decks) > 0:
	
	###calculate the minimum games played by all decks.
	min_len = min([len(deck.data) for deck in decks])
	
	###rating list, going to be filled with ratings of decks
	rating_list = []
	
	###go through each deck and calculate the rating.
	for deck in decks:
		rating = deck.get_rating(deck.data,min_len,factor) 	#calculates rating of last 'min_len' games
		rating_list.append(rating) 							#appends the deck rating to rating_list
		
	###update rating and ranking lists
	ranking.append(decks[rating_list.index(min(rating_list))]) 	#append ranking list with the worst performing deck of remaining decks
	del decks[rating_list.index(min(rating_list))]				#delete worst performing deck from deck-list, to compare remaining decks in next loop





########################################################################
### Output ###
########################################################################

'''
creates output.
'''

print('Ranking in decreasing order:')
print()

for deck in ranking[::-1]:
	print(str(deck.version) + '. version of ' + deck.player +"'s " + deck.deck_type + '-' + deck.hero)
