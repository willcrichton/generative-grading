import sys
sys.path.insert(0, '../..')

import generatorUtils as gu
import random
from base import Decision

class Program(Decision):
	def registerChoices(self):
		'''
		We add a dummy RV with only one value 
		to make the RNN code easier.
		'''		
		self.addChoice(self.ROOT_RV_NAME, {
			self.ROOT_RV_VAL: 1
		})

	def renderCode(self):		
		templateVars = {
			'Solution':self.expand('Solution'),
		}
		template = '''
		public class PythagoreanTheorem extends ConsoleProgram {{
			public void run() {{
				{Solution}
			}}
		}}
		'''
		return gu.format(template, templateVars)

		