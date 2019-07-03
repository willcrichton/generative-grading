import sys
sys.path.insert(0, '../..')

import generatorUtils as gu
import random
from base import Decision

# Decision: inputPrompt
# ------------------------
# There are lots of ways of writing the input prompt
# This is by no means an extensive list.
# List does not account for different punctuations.
class inputPrompt(Decision):
	def registerChoices(self):
		self.addChoice('inputPrompt', {
			'': 55, # empty string to keep simplest prompt unchanged
			'Enter ': 22,
			'enter value ': 11,
			'Enter value for ': 11,
		})

	def renderCode(self):
		templateVars = {
			'base':self.getChoice('inputPrompt'),
		}
		template = '{base}'
		return gu.format(template, templateVars)

