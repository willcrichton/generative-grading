import sys
sys.path.insert(0, '../..')

import generatorUtils as gu
import random
from base import Decision

class Solution(Decision):
	def renderCode(self):
		templateVars = {
			'mainPrompt': self.expand('mainPrompt'),
			'inputPrompt': self.expand('inputPrompt'),
			'exponential': self.expand('exponential'),
			'outputPrompt': self.expand('outputPrompt')
		}

		# assumes all students used doubles
		template = '''
		println("{mainPrompt}");
		double a = readDouble("{inputPrompt}a:");
		double b = readDouble("{inputPrompt}b:");
		double c = Math.sqrt({exponential} + {exponential});
		println("{outputPrompt}" + c);
		'''

		return gu.format(template, templateVars)
		
