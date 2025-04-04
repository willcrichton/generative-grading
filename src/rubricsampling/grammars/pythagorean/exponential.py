import sys
sys.path.insert(0, '../..')

import generatorUtils as gu
import random
from base import Decision

# Decision: exponential
# ------------------------
# Students may calculate exponentiation inline or use Math.pow()
class exponential(Decision):
	def registerChoices(self):
		if not self.hasChoice('usesMethod'):
			self.addChoice(f'usesMethod', {
				True : 5,     # they calculate the exponential inline
				False : 10    # they use Math.pow()
			})

	def updateRubric(self):
		method = self.getChoice('usesMethod')
		if not method:
			self.turnOnRubric('usesMath.Pow')
		else:
			self.turnOnRubric('usesInlineCalculation')

	def renderCode(self):		
		if self.getChoice(f'usesMethod'):
			return self.expand('mathPow', params=self.params)
		else:
			return self.expand('mathInline', params=self.params)


# Decision: mathPow
# ------------------------
# Students use of Math.pow()
# Alternate: var = self.getState('var')
class mathPow(Decision):
	def renderCode(self):		
		var = self.params['var']
		return f'Math.pow({var},2)'


# Decision: mathInline
# ------------------------
# Students use of inline command '*'
# Alternate: var = self.getState('var')
class mathInline(Decision):
	def renderCode(self):
		var = self.params['var']
		return f'{var}*{var}'


# def make_exponential(name):
# 	class exponential(Decision):
# 		def registerChoices(self):
# 			self.addChoice(f'{name}usesMethod', {
# 				True : 5,     # they calculate the exponential inline
# 				False : 10  # they use Math.pow()
# 			})
# 
# 		def renderCode(self):
# 			if self.getChoice(f'{name}usesMethod'):
# 				return '{mathPow}'
# 			else:
# 				return '{mathInline}'
# 
# 	exponential.__name__ = name
# 	return exponential
# 
# exponential = make_exponential('exponential')
# exponential2 = make_exponential('exponential2')

