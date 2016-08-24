# ex48
zed shaw's ex48

class Lexicon(object):

	def __init__(self):
		pass

	def scan(self, text):
		#When running test_directions, assert_equal(lexicon.scan("north"), [('direction', 'north')])
		#gets an AssertionError: None != [('direction', 'north')]
		#I need to get words that do not fit a value to return None.
		word_types = {'north': 'direction', 'south': 'direction', 'east': 'direction', 'west': 'direction', 
					'down': 'direction', 'up': 'direction', 'left': 'direction', 'right': 'direction', 
					'back': 'direction', 'go': 'verb', 'stop': 'verb', 'kill': 'verb', 'eat': 'verb', 
					'the': 'stop', 'in': 'stop', 'of': 'stop', 'from': 'stop', 'at': 'stop', 'it': 'stop', 
					'door': 'noun', 'bear': 'noun', 'princess': 'noun', 'cabinet': 'noun'}
		stuff = text.split()
		scanlist = []
		
		for i in stuff:
			if i in word_types:
				#I could either add to scanlist or just return it to match assert_equal
				#scanlist.append((word_types[i], i)) might be another option and return scanlist
				#return [(word_types[i], i)] doesn't work with a new list for multiple words, so
				#I might have to append to the list to make it work.
				scanlist.append((word_types[i], i))
				return scanlist
			else:
				return 'None'
			
			
				
				
