########################################################################
### Class for HS-decks###
########################################################################
class HS_Deck():
	
	'''
	Class for all HS-decks. Saves deck properties. 
	'''
	
	####################################################################
	### Initialization method###
	####################################################################
	def __init__(self,player,hero,deck_type,version):
		
		'''
		Saves deck-properties to object. 
		'''
		
		self.player 	= player 	#player who invented the deck
		self.hero 		= hero		#class of deck
		self.deck_type	= deck_type	#type of deck
		self.version 	= version	#version of this deck
		
	
	
	
	
	####################################################################
	### read in data ###
	####################################################################
	def read_file(self,data):
		
		'''
		Reads all deck-specific data out of the data file.
		'''

		deck_data = data.ix[(data['Inventor']	== self.player) 
		& 	(data['Class (me)'] 				== self.hero)
		& 	(data['Type (me)'] 					== self.deck_type)
		& 	(data['Version'] 					== self.version)
		]
		
		self.data = deck_data
	
	
	
	
	
	
	####################################################################
	### calculate rating ###
	####################################################################
	def get_rating(self,data,min_len,factor):
		
		'''
		Calculates rating of the deck in last 'min_len' games (=normed data)
		'''
		
		###the last 'min_len' games of data set is the normed data set
		data_norm = data.tail(min_len)
		
		###set counter and rating value to zero
		rating 	= 0
		counter = 0
		
		###go through all lines of the normed data 
		for index, row in data_norm.iterrows():
			
			###if win, add a value to rating, according to formula
			if row['Outcome'] == 'Win':
				rating += (counter + 1)/len(data_norm['Outcome'])/(0.425*row['Day of month']+((row['Rank (me)']+ row['Rank (enemy)'])/2))*factor 

			###if loss, substract value to rating, according to formula
			elif row['Outcome'] == 'Loss':
				rating -= (counter + 1)/len(data_norm['Outcome'])*(0.425*row['Day of month']+((row['Rank (me)']+ row['Rank (enemy)'])/2))/factor 
			
			###if outcome is neither win, nor loss, there must be a spelling mistake
			else:
				print('Something wrong with spelling of Outcome in the ' + index + 'th line of the dataset')
			
			###after adding the game to rating, increase the counter by 1
			counter += 1 

		return rating


