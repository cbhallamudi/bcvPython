#if condition:
#	statements

#if the relational or comparisional condition is true, the statements inside the if block executes. But if the condition is false, this won't do anything

if 5<6:
	print("Given Condition is true")

#if the relational or comparisional condition is true, the statements inside the if block executes. Else if the condition is false, then the else block will get executed.

if 5>6:
	print("Given Condtion is true")
else:
	print("Given Condition is false")

#if we have to compare a single variable inside more than one condition, we can use "elif"

if 5>6:
	print("5 is greater than 6")
elif 5<6:
	print("6 is greater than 5")
else:
	print("No result")

#single line if statement:
if (10>9) : print("The condition is wrong")



