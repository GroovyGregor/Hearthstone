###parameter for the best_decks.py program, which rates the different decks.

data_file	= 'HS Stats - Tabellenblatt1.csv'	#file with data from ladder
factor		= 20								#factor for calculating the rating
min_len		= 10								#minimum number of times a matchup must have been played to be considered





########################################################################
### decks ###
########################################################################

deck1 = ['Lifecoach','Warrior','Dragon',1]
deck2 = ['ThijsNL','Warlock','Reno',1]
deck3 = ['ThijsNL','Priest','Dragon',1]
deck4 = ['Lifecoach','Shaman','Jade',1]
deck5 = ['ThijsNL','Warrior','Pirate',1]
deck6 = ['BlackFireIce','Shaman','Aggro',1]

###list of all HS-deck for looping purposes
decks = [deck1,deck2,deck3,deck4,deck5,deck6]
