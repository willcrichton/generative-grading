import sys
sys.path.insert(0, '../..')

import generatorUtils as gu
import random
from base import Decision

class Solution(Decision):
	def registerChoices(self):
		self.addChoice('firstVar', {
			'a': 1,
			'x': 1
		})
		self.addChoice('secondVar', {
			'b': 1,
			'y': 1
		})		

	def renderCode(self):
		self.addState('aUsed', False)
		self.addState('var', None)

		firstVar = self.getChoice('firstVar')
		secondVar = self.getChoice('secondVar')
			
		self.setState('var', firstVar)
		exponential1 = self.expand('exponential')
		self.setState('var', secondVar)
		exponential2 = self.expand('exponential')

		templateVars = {
			'mainPrompt': self.expand('mainPrompt'),
			'inputPrompt': self.expand('inputPrompt'),
			'exponential1': exponential1, #self.expand('exponential', params={'var': firstVar}),
			'exponential2': exponential2, #self.expand('exponential', params={'var': secondVar}),
			'outputPrompt': self.expand('outputPrompt'),
			'firstVar': firstVar,
			'secondVar': secondVar
		}	

		# assumes all students used doubles
		template = '''
		println("{mainPrompt}");
		double {firstVar} = readDouble("{inputPrompt}a:");
		double {secondVar} = readDouble("{inputPrompt}b:");
		double c = Math.sqrt({exponential1} + {exponential2});
		println("{outputPrompt}" + c);
		'''

		return gu.format(template, templateVars)
		
