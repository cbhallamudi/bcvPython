#to use command line arguments
import sys

print (sys.argv)

#to print
print("This is python basic page")

#class name starts with an uppercase example Myclass
#if identifier starts with an underscore it is a private identifier. Example _privateVar
#if identifier starts with two underscores it is a strong private identifier. Example __strongprivateVar
#if identifier starts with two underscores and followed by two underscores more, a language-defined special name. Example __privateVar__

if True:
	print("Done")
	print("Damage")	
else:
	print("Damage")	
	print("Undone")	

variable1 = "This is "+\
	"a basic "+\
	"Python file."

variable2 = '''This is another statement
spanning more than two lines
using triple quotes'''

# print(variable1)

variable3 = 5;print(variable3)

#assigning single value to multiple variables
var1 = var2 = var3 = 10

# print(var2)

#declaring and assigning multiple variables in the same line

var4,var5 = 5,6

print(var5)

#to delete one or more variables

# del var3,var5

# in to check if some value exists in a sequence of characters or a set of numbers, returns true

var6 = "This is Chaitanya"
var7 = "This is chaitanya"

# if("Cha" in var6):
# 	print(var6)
# else:
# 	print("Not found")	

# if("@" not in var6):
# 	print("True! Not a mailid")
# else:
# 	print("False! No special characters allowed")

#id(variable) will generate a random number for that instance.

# print(id(var6))
# print(id(var7))

#is and is not will check if the values of the variables are same to same.
if(var6 is not var7):
	print("Both variables doesn't have same values")	
else:
	print("Both have same values")
	


