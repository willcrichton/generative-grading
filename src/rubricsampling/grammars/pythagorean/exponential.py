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
		self.addChoice('usesMethod', {
			True : 5,     # they calculate the exponential inline
			False : 100   # they use Math.pow()
		})

	def renderCode(self):
		if self.getChoice('usesMethod'):
			return '{mathPow}'
		else:
			return '{mathInline}'


# Decision: mathPow
# ------------------------
# Students use of Math.pow()
class mathPow(Decision):
	def renderCode(self):
		aUsed = self.getState('aUsed')
		if aUsed == False:
			self.addOrSetState('aUsed', True)
			return 'Math.pow(a,2)'
		else:
			return 'Math.pow(b,2)'


# Decision: mathInline
# ------------------------
# Students use of inline command '*'
class mathInline(Decision):
	def renderCode(self):
		aUsed = self.getState('aUsed')
		if aUsed == False:
			self.addOrSetState('aUsed', True)
			return 'a*a'
		else:
			return 'b*b'


