class Lexicon(object):

	def __init__(self):
		pass

	def convert_number(self, num):
		try:
			return int(num)
		except ValueError:
			return None
			
	def scan(self, words):
		direction = ['north', 'east', 'south']
		verb = ['go', 'kill', 'eat']
		stop = ['the', 'in', 'of']
		noun = ['bear', 'princess']
		stuff = words.split()
		list = []

		for s in stuff:
			if s in direction:
				list.append(('direction', s))
			elif s in verb:
				list.append(('verb', s))
			elif s in stop:
				list.append(('stop', s))
			elif s in noun:
				list.append(('noun', s))
			elif s.isdigit():
				list.append(('number', lexicon.convert_number(s)))
			else:
				list.append(('error', s))
				
		return list

lexicon = Lexicon()
