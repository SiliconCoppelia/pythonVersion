"""
	__init__ Class
	Current Dimensions: Ethics, Affordances, and Aesthetics
	Current Settings of Coppeélia: 
			1. Coppélia prefers good-looking subjects
			2. Coppélia prefers kind and friendly subjects
			3. Coppélia wishes to make friends or date with agents
			4. Coppélia is an individual with kind and friendly personality, and a smart subject
	To-Do: 
			1. Formulation of The Order Of Saying Things In Ethics
			2. ....
"""

# Import Dependencies
# https://stackoverflow.com/questions/43023970/builtin-function-or-method-object-has-no-attribute-randrange
import random as rand
from tkinter import *

# Import Classes
import sys
sys.path.append('./features')
from ethics import *
from affordance import *


Greet = "Hi there, before we get started, allow me to know you more by asking you some questions."
Question1 = "Do you think killing is always illegal? Why?"
Question2 = "What starts with \"E\" and ends with \"E\" but only has one letter in it?"
Question3 = "How would you describe yourself in three words?"
# Reference: https://www.buzzfeed.com/spenceralthouse/trick-question-iq-test


class GUIForQuestionsAndCV():

	window = Tk(className = 'Questions from Coppélia')
	answers = []
	
	def mainLoop(self):
		self.window.mainloop()

	def windowSettings(self):
		self.window.geometry("750x250")
		self.window.configure(bg = "#f4f2ea")
		
		# Label(text = Greet).pack()
		self.questionsWidgets(Question1)
		self.questionsWidgets(Question2)
		self.questionsWidgets(Question3)

		self.buttonWidgets()

	def questionsWidgets(self, Questions):
		Label(text = Questions, font=("Dosis", 20), bg = "#f4f2ea", fg = "#000a39").pack(side= TOP, anchor="w")
		self.answers.append(Entry().pack(side= TOP, anchor="w"))

	def buttonWidgets(self):
		Submit = Button(self.window, text = "Submit", width=20, height=2, activebackground='#AA2E00', activeforeground='#AA2E00')
		Submit.pack(side= TOP, anchor="w")
		Submit.bind("<Button-1>", self.passAnswer)

	def passAnswer(self, event):
		# print(' '.join(self.answers.get()))
		self.window.destroy()


class Coppelia():

	ethics = Ethics()
	affordance = Affordance()

	greetings = "Hi, I'm Coppélia."
	goal = "I want to be friends with you"

	def __init__(self):
		print(self.greetings)

	def setEthics(self, score):
		self.ethics.setEthics(score)

	def coppeliaSpeaksEthics(self, posOrNeg):
		self.ethics.coppeliaSpeaksEthics(posOrNeg)

	def setAffordance(self, score):
		self.affordance.setAffordance(score)

	def coppeliaSpeaksAffordance(self, posOrNeg):
		self.affordance.coppeliaSpeaksAffordance(posOrNeg)

	# Reference of random fractions between two values: 
	# https://stackoverflow.com/questions/6088077/how-to-get-a-random-number-between-a-float-range


# GUIWindow = GUIForQuestionsAndCV()
# GUIWindow.windowSettings()
# GUIWindow.mainLoop()

coppelia = Coppelia()
# coppelia.setEthics(rand.uniform(0, 1))
# coppelia.coppeliaSpeaksEthics("positive")
# coppelia.coppeliaSpeaksEthics("negative")

coppelia.setAffordance(rand.uniform(0, 1))
coppelia.coppeliaSpeaksAffordance("positive")
coppelia.coppeliaSpeaksAffordance("negative")






