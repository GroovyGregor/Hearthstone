###program to count number of games played by each deck

'''
'''





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
lengths		= []						#will contain lengths of all deck specific data
decks 		= []						#will be filled with a HS-objective for each deck

###paraemter
deck_par = parameters.decks				#all of my decks in a list




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
	lengths.append(len(deck.data))
	
lengths = np.array(lengths)			#transform to numpy array to be able to use np.argsort
indices = np.argsort(lengths)[::-1]	#contains indices that would sort the lengths-array





########################################################################
### output ###
########################################################################

'''
'''

###go through the sorted indices-array
for index in indices:
	print('length: ' + str(lengths[index]) +'         '+ str(decks[index].version) + '. version of ' + decks[index].player + "'s " + decks[index].deck_type + '-' + decks[index].hero)
