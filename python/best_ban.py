###program to decide which class to ban





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
### parameters, data ###
########################################################################

'''
Defines parameters and opens data 
'''

###parameters
data_file 		= parameters.data_file 		#file name
factor			= parameters.factor			#factor for calculation of rating
min_len			= parameters.min_len		#threshold --> minimum number of games for a matchup, to be considered for the rating calculation
deck_par		= parameters.decks			#all of my decks

###data
data 			= pd.read_csv(data_file)	#open data file

###dicts
hero_rating		= {}						#will be filled with summed ratings against each enemy class

###lists
ranking			= []						#will be filled with decks in ranked order
lengths			= []						#will be filled with lengths of data for each matchup (to find minimum)
decks			= []						#will be filled with HS-objective for each of my decks




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
### Enemy classes ###
########################################################################

'''
Define enemy classes.
'''

enemy_classes 	= ['Warrior','Rogue','Priest','Shaman']	#classes of enemy





########################################################################
### read in data ###
########################################################################

'''
reads in for each deck specific data
'''

###get deck specific data
for deck in decks:
	deck.read_file(data)
	




########################################################################
### find minimum length ###
########################################################################

'''
Ratings are only comparable for the same number of games. Find minimum
number of games for all possible matchups.
'''

###loop through my decks
for deck in decks:
	
	###loop through enemy classes
	for hero in enemy_classes:
		
		data = deck.data.ix[(deck.data['Class (enemy)'] == hero)] #data of this matchup

		###if length of data is larger than threshold, append it to lengths-list, to find minimum
		if len(data) >= min_len:
			lengths.append(len(data))
			
###find minimum length
tail = min(lengths)





########################################################################
### get best ban ###
########################################################################

'''
gets best class to ban, by looping through all enemy classes and 
for each enemy class, add ratings of all my decks against this class.
Best class to ban is then the enemy class, which resultet in minimum
rating.
'''

###loop through enemy_classes
for hero in enemy_classes:
	rating = 0 #set rating-sum to zero
	
	###loop through my decks
	for deck in decks:
			
		data = deck.data.ix[(deck.data['Class (enemy)'] == hero)] #get data for this matchup

		###if threshold-condition is satisfied, calculate rating
		if len(data) >= min_len:
			rating += deck.get_rating(data,tail,factor)
		
	###after looping through all my decks, save rating against this enemy class (hero)
	hero_rating[hero] = rating		
	

###find best class to ban
ban = min(hero_rating, key=lambda k: hero_rating[k])





########################################################################
### Output ###
########################################################################

'''
Output of result
'''

print('Ban: ' + ban)
