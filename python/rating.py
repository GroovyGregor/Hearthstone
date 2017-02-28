###get rating of each deck





########################################################################
### modules ###
########################################################################

'''
import modules and functions
'''

import numpy as np
import pandas as pd
import parameters
from HSModule.HSDeck import HS_Deck





########################################################################
### parameters, data ###
########################################################################

'''
Defines parameters and opens data 
'''

###data
data_file 	= parameters.data_file 		#file name
data 		= pd.read_csv(data_file)	#open data file


###lists
decks		= []						#will be filled with HS-objective for each deck
ratings		= []						#contains rating of decks in same order as decks are saved in 'decks'-list

###parameter
factor		= parameters.factor			#factor for calculation of rating
deck_par	= parameters.decks			#all of my decks in a list





########################################################################
### Create Deck-Objectives ###
########################################################################

'''
Creates a Hearthstone_deck - objective for each Hearthstone deck.
'''

###create a HS-objective for each deck
for deck in deck_par:
	decks.append(HS_Deck(deck[0],deck[1],deck[2],deck[3]))





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
Calculates a rating for each deck. 
'''

###get rating of all decks
for deck in decks:
	ratings.append(deck.get_rating(deck.data,len(deck.data),factor))

###get indices of ratings, if sorted by max
ratings = np.array(ratings)			#form to numpy array to be able to use argsort
indices = np.argsort(ratings)[::-1]	#get indices of sorted rating array





########################################################################
### Output ###
########################################################################

'''
creates output.
'''

print('Ranking of decks in decreasing order:')
print()

###loop through sorted indices array
for index in indices:
	print('rating: ' + str(ratings[index]) + '            ' + str(decks[index].version) + '. version of ' + decks[index].player +"'s " + decks[index].deck_type + '-' + decks[index].hero)

