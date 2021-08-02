#Called dictionaries in python, this is where you can do key-value pairs
#like in PHP. Format is as follows
#{"key" : "value", "another key" : "another value"}

medic = {"name" : "Medic", "hp" : 200, "skill" : "defib"}
engi = {"name" : "Engineer", "hp" : 175, "skill" : "ladder"}

#get would track if a key exists on a dictionary and throws its value
#and if none, it lists the information on the second value

check_med_wep = medic.get("weapon", "not recorded")
print(f"{medic['name']} weapon status: {check_med_wep}")
#weapon does not exist as a key so "not recorded"

check_med_hp = medic.get("hp", "not recorded")
print(f"{medic['name']} HP status: {check_med_hp}")
#hp does exist as a key and will return its value

print() #newline

print(f"{engi['name']} special skill: {engi.get('skill', 'no extra skills')}")
#prints current skill. Yes, either using brackets [] or get[] can do

engi.update({"skill" : "wall", "comment" : "Engineers can now build walls to defend"})
print(f"{engi['name']} updated!")
print(f"{engi['name']} special skill: {engi.get('skill', 'no extra skills')}")
print(f"{engi['name']} comment: {engi.get('comment', 'no comment')}")
#updates the key to a new value
#update can accept multiple values for a dictionary or just single entry
#like engi['comment'] = 'Engineers can now build walls to defend'

engi.pop("comment")
print(f"{engi['name']} comment removed: {engi.get('comment', 'no comment')}")
#pop removes the value for a specific key, can be stored to variable
#this should have no comment

print()

print(f"Reading {medic['name']} dictionary (hashmap) stats...")
for key, val in medic.items():
    print(f"{key}: {val}")
#using .items() on a dictionary is the right way to get
#the key and values at once to loop from
