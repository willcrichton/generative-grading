import sys
sys.path.insert(0, '../..')

import generatorUtils as gu
import random
from base import Decision

# Decision: mainPrompt
# ------------------------
# There are lots of ways of writing the main prompt
# This is by no means an extensive list
# List does not account for different punctiations
class mainPrompt(Decision):
	def registerChoices(self):
		self.addChoice('mainPrompt', {
			'Enter values to compute the Pythagorean Theorem.': 70,
			'This program finds the hypotenuse, C, of a triangle with sides A and B.': 15,
			'This program runs the Pythagorean Theorem. Choose values a and b.': 15,
		})

	def renderCode(self):
		templateVars = {
			'base':self.getChoice('mainPrompt'),
		}
		template = '{base}'
		return gu.format(template, templateVars)

