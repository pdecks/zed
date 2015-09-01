# Exercise 37: Symbol Review

# KEYWORDS
# - Write what each does (from memory)
# - Search online and confirm what it does
# - Use each in a small Python program
# 	keywords are reserved words of the language that cannot be used as 
#	ordinary identifiers.


# and
# 'and' is a logic keyword that chains together multiple conditions
# represents the INTERSECTION of conditions: All conditions in a Boolean
# expression must be met
# the AND truth table is as follows
# 	True and True --> True
# 	True and False --> False
# 	False and True --> False
# 	False and False --> False
# 		the following program would return "True"
#			('test' == 'test') AND ('testing' != 'resting') AND (2 == (6 / 3))


# del
# deletes objects (other than local variabls) more clearly than assigning 'None' to the value
# ex: del list_item[4]
# ex: del dictionary["alpha"]
# compare: del foo # intent to remove from scope
# to:	   foo = None # dead code? intent not clear


# from
# used when importing specific variables, classes, or functions from a module
# from MODULE-Z import ABCD 


# not
# 'not' is a logic keyword that negates a Boolean value
# the NOT truth table is:
# 	not False --> True
# 	not True --> False


# while
# 'while <condition>' is a loop keyword that performs an
# action WHILE the condition is met (controlling the flow of the program)
#	the following program would increment the variable 'oranges' 
#   until it is equal to apples
# 		while apples > oranges:
#		oranges += 1


# as
# used when IMPORTing modules to rename them, often with shorter aliases
# ex: import pandas as pd 


# elif
# "else if" used after an "if" statement but before an "else" statement
# If the first test evaluates to False, then it continues with the next one
# 	if <condition 1>:
#		<state 1>
#	elif <condition 2>:
#		<state 2>
#	else:  # neither condition 1 nor 2 is met
#		<default state>


# global
# access variables defined outside functions
# ex: def set_globvar_to_one():
#		global globvar # needed to modify global copy of globvar
#		globvar = 1
#	  def print_globvar():
#		print globvar # no need for global declaration to read value of globvar


# or
# a logic operator that represents the UNION of conditions
# at least one condition must be met
# the OR logic table is:
#	True or True --> True
#	True or False --> True
#	False or True --> True
# 	False or False --> False


# with
# control-flow structure whose basic structure is:
# with expression [as variable]: with-block
#  with open('output.txt', 'w') as f:
#      f.write('Hi there!')
# The above with statement will automatically close the file after the
# nested block of code. (Continue reading to see exactly how the close
# occurs.) The advantage of using a with statement is that it is guaranteed
# to close the file no matter how the nested block exits. If an exception
# occurs before the end of the block, it will close the file before the
# exception is caught by an outer exception handler. If the nested block
# were to contain a return statement, or a continue or break statement,
# the with statement would automatically close the file in those cases, too.


# assert
# used for debugging purposes
# assert a_condition # ... you're telling the program to test that condition
#					 # and trigger an error if the condition is false
# triggers an AssertionError that can include an optional message


# else
# used in a conditional statement after an if-statement
#	if <condition 1>
#		<state 1>
#	else: # condition 1 is not met
#		<state 2>


# if
# a conditional operation
#	if <condition 1>
#		<state 1>
#	else: # condition 1 is not met
#		<state 2> 	


# pass
# does nothing --> often used as a placeholder
# >>>if 'a':
# >>>    do_something()
# >>>elif 'b':
# >>>    #TODO: implement do_something_else()
# >>>    pass
# >>>elif 'c':
# >>>    quit_foo()


# yield
# is used with generators
# https://www.jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/
# return implies that the function is returning control of execution to the
# point where the function was called. "Yield," however, implies that the
# transfer of control is temporary and voluntary, and our function expects to
# regain it in the future.


# break
# used to jump out of a loop 

# except
# catches the exception and executes code

# import
# used to import modules
# ex: import pandas

# print
# used to produce standard output on the computer screen
# ex: print "Hello World!"
# > Hello World!

# class 
# used to create new user-defined objects

# exec
# executes Python code dynamically

# in	
# used with loops to proceed systematically through a list

# raise
# create a user-defined exception

# continue
# used to interrupt the current cycle, without jumping out of the whole cycle.
# new cycle will begin

# finally
# is always executed in the end. used to clean up resources.

# is
# tests for object identity

# return
# used at the end of a function to pass information back to the function call
# ex: def my_function():
#		return 1 + 1
# answer = my_function # answer = 2

# def 
# used to mark the start of a function
# ex: def my_function():

# for 
# a for-loop marches through a set of operations in the block for a given range
# ex: for apples in fruits:
#		print apples

# lambda
# creates a new anonymous function

# try
# specifies exception handlers