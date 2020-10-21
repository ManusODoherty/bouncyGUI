"""
bouncygui.py
Manus O'Doherty
10/20/2020
gui base version of bouncy.py app from chapter 3
program will calculate the total distance travelled by a bouncy ball
user will input:
	the starting height of the ball
	how bouncy the ball is
	how many bounces the ball will make
the output should be the total distance the ball travels
"""

from breezypythongui import EasyFrame
from tkinter.font import Font

class Bouncy(EasyFrame):

	def __init__(self):
		"""sets up window and widgets"""
		EasyFrame.__init__(self, title = "Bouncy App", background = "lightblue")
		myFont = Font(family = "Courier New", size = 16, weight = "bold")
		self.addLabel(text = "Bouncy Experiment", row = 0, column = 0, columnspan = 2, background = "lightblue")
		self.addLabel(text = "initial height:", row = 1, column = 0, background = "lightblue")
		self.addLabel(text = "Bounciness Index", row = 2, column = 0, background = "lightblue")
		self.addLabel(text = "No. of Bounces", row = 3, column = 0, background = "lightblue")
		self.addLabel(text = "Total Distance:", row = 5, column = 0, background = "lightblue")

		self.height = self.addFloatField(value = 0.0, row = 1, column = 1)
		self.index = self.addFloatField(value = 0.0, row = 2, column = 1)
		self.bounces = self.addIntegerField(value = 0.0, row = 3, column = 1, width = 20)
		self.distance = self.addFloatField(value = 0.0, row = 5, column = 1, precision = 2, state = "readonly")

		#add the command button
		self.addButton(text = "Compute", row = 4, column = 0, columnspan = 2, command = self.bounce)

	#event handling method
	def bounce(self):
		"""calculates the total distance traveled given the inputs"""
		#input phase
		height = self.height.getNumber()
		index = self.index.getNumber()
		bounces = self.bounces.getNumber()

		#accumulator variable for total distance traveled
		totalDistance = 0.0

		# for loop to determine the ottal distance traveled
		for count in range(bounces):
			totalDistance += height
			height *= index
			totalDistance += height

		self.distance.setNumber(distance)

# definition of the main() function
def main():
	Bouncy().mainloop()

#global call to main()
main()
