"""
Default Values


You are given a function for a hotel booking service. The First argument is the number of people staying in the hotel room, the second is the number of days, and the third is for breakfast option choice.

Taking into account that visitors do not always mention their breakfast choice, we need to set the "Egg Sandwiches" option as the default.
Complete the function so that the given code works correctly.
"""

def book(people, days, breakfast = "Egg Sandwiches"):
	print("People:", people)
	print("Days:", days)
	print("Breakfast:", breakfast)

book(5,3, "Peanut Butter Bites")
book(4,5)