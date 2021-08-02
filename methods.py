#aka functions

def soldier_categ(*args):
    print(args)
#positional arguments
#this means the method can accept multiple types of arguments
print("Reading soldier category entries:")
soldier_categ("Leader", "Bomber","Scout")

def soldier_info(**kwargs):
    print(kwargs)
print("\nReading soldier information entries:")
soldier_info(name="Bomber",hp=300,skill="rocket")
#key-word arguments
#this means the method can accept multiple types of dictionary arguments
#which includes {"hp" : 150} but formatted as hp=150 inside arguments

scout_name = ["Scout"]
scout_info = {"hp" : 175, "skill" : "infrared"}

def soldier_complete(*args, **kwargs): #args=soldier name, #kwargs=soldier info
    print(args)
    if not kwargs: #if kwargs evaluates to False or empty
        print("No soldier info entered")
    else:
        print(kwargs)

print("\nInput scout name and scout info separately:")
soldier_complete(scout_name, scout_info)
#You'd initially expect it'll enter scout_name on *args,
#and scout_info on **kwargs, because of comma separation right?
#WRONG.
#because *args came first, and it accepts multiple types of arguments
#it'll count the dictionary entry of scout_info into *args only, it'll
#never reach **kwargs
#hence "if not kwargs" is evaluated and no soldier info entered appears

print("\nInput scout name and scout info successfully:")
soldier_complete(*scout_name, **scout_info)
#So what you must use instead is actually the above
#you specify which variables are meant to be in the *args and **kwargs
#to prevent confusion

