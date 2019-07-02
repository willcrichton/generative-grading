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
		return 'Math.pow(x,2)'


# Decision: mathInline
# ------------------------
# Students use inline command '*'
class mathInline(Decision):
	def renderCode(self):
		return 'x*x'


