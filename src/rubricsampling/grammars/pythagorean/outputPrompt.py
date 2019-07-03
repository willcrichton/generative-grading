import sys
sys.path.insert(0, '../..')

import generatorUtils as gu
import random
from base import Decision

# Decision: outputPrompt
# ------------------------
# There are lots of ways of writing the output prompt
# This is by no means an extensive list.
# List does not account for different punctuations.
class outputPrompt(Decision):
	def registerChoices(self):
		var = self.params['var']
		self.addChoice('outputPrompt', {
			f'{var}=': 55, 
			f'{var}:': 22,
			'The answer is': 11,
			'The hypotenuse is ': 11,
		})

	def renderCode(self):
		templateVars = {
			'base':self.getChoice('outputPrompt'),
		}
		template = '{base}'
		return gu.format(template, templateVars)

