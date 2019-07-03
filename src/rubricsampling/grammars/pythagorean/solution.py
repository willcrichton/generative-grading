import sys
sys.path.insert(0, '../..')

import generatorUtils as gu
import random
from base import Decision

class Solution(Decision):
	# This function probabilistically chooses variable names, number types, 
    # and print function to display in the program.
	def registerChoices(self):
		self.addChoice('firstVar', {
			'a': 1,
			'x': 1
		})
		self.addChoice('secondVar', {
			'b': 1,
			'y': 1
		})
		self.addChoice('thirdVar', {
			'c': 1,
			'z': 1
		})
		self.addChoice('numType', {
			'int': 1,
			'double': 1
		})
		self.addChoice('functionType', {
			'readInt': 1,
			'readDouble': 1
		})
		self.addChoice('printFunction', {
			'println': 1,
			'print': 1
		})				

	def renderCode(self):
		# Initialize var
		self.addState('var', None)

		# Probabilistically chooses values
		firstVar = self.getChoice('firstVar')
		secondVar = self.getChoice('secondVar')
		thirdVar = self.getChoice('thirdVar')
		numType = self.getChoice('numType')
		functionType = self.getChoice('functionType')
		printFunction = self.getChoice('printFunction')

		# Having chosen, assigns these values to var 
		# (creates a pair in the State dict)
		self.setState('var', firstVar)
		self.setState('var', secondVar)
		self.setState('var', thirdVar)

		# Alternate:
		# exponential1 = self.expand('exponential')
		# exponential2 = self.expand('exponential')
		templateVars = {
			'mainPrompt': self.expand('mainPrompt'),
			'inputPrompt': self.expand('inputPrompt'),
			'exponential1': self.expand('exponential', params={'var': firstVar}),
			'exponential2': self.expand('exponential', params={'var': secondVar}),
			'outputPrompt': self.expand('outputPrompt', params={'var': thirdVar}),
			'firstVar': firstVar,
			'secondVar': secondVar,
			'thirdVar': thirdVar, 
			'numType': numType,
			'functionType': functionType,
			'printFunction': printFunction
		}	

		template = '''
		{printFunction}("{mainPrompt}");
		{numType} {firstVar} = {functionType}("{inputPrompt}{firstVar}:");
		{numType} {secondVar} = {functionType}("{inputPrompt}{secondVar}:");
		{numType} {thirdVar} = Math.sqrt({exponential1} + {exponential2});
		{printFunction}("{outputPrompt}" + {thirdVar});
		'''

		return gu.format(template, templateVars)
		
