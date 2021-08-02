#unlike with other programming languages that require parentheses ()
#python does not need it for if-else statements, but it works with it

fake = False
empty = None
stmt = 0
f = 69
k = 420
hz = [60, 75, 90, 120, 144, 240, 360]

if k > f:
    print(f"no parentheses if condition: {k} > {f}")
if (k > f):
    print(f"with parentheses if condition: {k} > {f}")

if not k==hz[5]:
    print(f"variable {k=}, not {hz[5]}")
#not can be used in place of != inequality
#or just evaluating if a statement is false and accept it if false

#for fstrings in pythong, using {var_name=}
#will print the variable name with the actual value of it directly'
#you must include the = sign
#otherwise it will just print value, period

#-------------------
#CONDITIONALS

if fake == False:
    print(f"Fake == {fake}, empty == {empty}")
#evalutes to print the fact that it is false

if not empty:
    print("empty will also evaluate to False")
#while empty is strictly set to None, which means using "if empty == None"
#will be skipped by the program

#if you use "if not empty"
#it will like on the above example, try to evaluate to false
#and None will evaluate to False in this specific way, so it will print
#the statement, it will not skip

if stmt == 0:
    print("0 is also false")
else:
    print("True bruh")
#What evals to False:
# * any variable = False
# * any variable = None
# * any variable = 0
# * any variable = '', (), [] which is an empty list or tuple
# * any variable = {} empty dict


#-------------------
#LOOPING

