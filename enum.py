import enum_mod as en
#IMPORTING scripts and libraries
#any script in same directory can be imported as a module
#you can use "import enum_mod" as is to import entire file
#but you can also use "import enum_mod as em"
#so em becomes the one you can use to get functions out of it
#to call more easily
from enum_mod import remove_instance as rm
#alternatively if you only need a specific function
#then you can use "from enum_mod import remove_instnce"
#from the actual file and use import for specific function

soldiers = ["Medic", "Engineer", "Bomber", "Scout"]
name_to_find = "Scout"
name_to_clear = "Bomber"

ndex = en.seek_instance(soldiers, name_to_find)
#notice that instead of usign enum_mod.seek_instance which also works
#en.seek_instance works as well
if ndex == -1:
    print("{} does not belong on the soldiers list".format(name_to_find))
else:
    print(f"{name_to_find} found on the soldier list, entry {ndex}")
#This reaches the else statement as the seek_instance function
#will find one item whose value equals the name of "Scout"
#and prints the key, which in this case is its number position on the array
#notice above it is at soldiers[3] hence the number 3

ndex_cleared = rm(soldiers, name_to_clear)
#notice that rm is used to call remove_instance function
#that also is from enum_mod file. Yes this is redundant to do
#but this is only an example

if ndex_cleared == -1:
    print("{} already doesn't belong on soldiers list".format(name_to_clear))
else:
    print(f"{name_to_clear} found and deleted on the soldier list, entry {ndex_cleared}")
    print("Updated soldiers list is as follows:")
    for n in soldiers:
        print(f"- {n}")
#this also evaluates to else statement
#the reason being that in the list it finds Bomber value with key being its
#position in the array as soldiers[2]
#and it pops it out