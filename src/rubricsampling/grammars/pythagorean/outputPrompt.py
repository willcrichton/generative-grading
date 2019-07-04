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
		self.addChoice('outputPrompt', {
			'a': 55, 
			'b': 22,
			'c': 11,
			'd': 11,
		})

	def renderCode(self):
		var = self.params['var']
		prompts = {
			'a': f'{var}=',
			'b': f'{var}:',
			'c': 'The answer is',
			'd': 'The hypotenuse is '
		}
		templateVars = {
			'base': prompts[self.getChoice('outputPrompt')],
		}
		template = '{base}'
		return gu.format(template, templateVars)

