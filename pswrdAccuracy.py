'''Allowes you to practice your password.
Input: correct password a spesified amount of times
Output: times password was entered incorrectly and stats'''
import sys
def check (): 
	correct = str(input("Please enter the correct password: "))
	repeat = int( input("Enter the minimum amount of times you need to enter your password correctly: ") )
	count = 0
	incorrect = 0
	while count < repeat:
		arg = str(input("Enter attempt: "))
		if arg == "exit":
			print("Exit program.")
			break
		if arg == correct:
			count = count + 1
			print("correct")
		else:
			print("incorrect")
			incorrect = incorrect + 1
	print("Done. Incorrect attempts: " + str(incorrect))
	print("Accuracy: " + str( count / (count + incorrect) ) )
