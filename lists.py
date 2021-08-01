#in Python, what's traditionally known as array is called a list
#there's also tuples (unordered lists) and sets {}
#but lists are the most common type in Python
#this is one reason why Python isn't actually good to start as a language
#because other programming languages use the common term for array

names = ["Hannah", "Anya", "Irina"]
names_new = ["Olivia", "Faye", "Laine"]

names_new.append("Nicole")
#adds to end automatically
#of note is if you append another list, it will keep the list as is
#and causes it to be multidimensional

names_new.insert(0, "Mikhaila") #adds to a specific position in the list (e.g. 0=start)

print(f"Updated new names list: {names_new}") #prints the updated list of new names

#-------------------
names.extend(names_new)
#use this to add items from another list but without causing it
#to be multidmensional so it'sm all under one list for easy sorting/seeking

print(f"Updated overall names list: {names}") #prints updated list of names overall

#-------------------
names.remove("Laine")
#removes specific item from list

print(f"Removed Laine from names. Updated names list: {names}") #updated list

#-------------------
last_name = names.pop()
#removed last item from list. This can be put into a variable for use

print(f"Popped out last item from list (which is {last_name}). Updated names list: {names}")
#updated list

#-------------------
names.sort()
#sort() from first to last letters or ascending order for numbers
#take note, this changes the actual list permanently

print(f"Names in alphabetical order: {names}")

#-------------------
names_z_to_a = sorted(names, reverse=True)
#sorted() must be used in order to prevent the original list from changing
#and instead save the results to another variable. the reverse=True is optional
#it is not required. It only is there to reverse order/descending,
#instead of alphabetical or ascending,
print(f"Names in reverse alphabetical order: {names_z_to_a}")

#-------------------
print(f"Names list enumerated: ")
for ndex, name in enumerate(names, start=1):
    print(f"{ndex}. {name}")
#you don't need to use enumerate but in here this allows getting index values
#that can be used to also print accordingly.
#start=1 is optional, NOT required. This only puts the array on starting value
#of 1 instead of default 0

#-------------------
names_raw = "Jonathan, Kyla, Irina, Markus"
names_extracted = names_raw.split(", ")
#you can get list from a string via split function of list and parsing using character
print(f"Acquired list of separate names from string. Separate list is now: {names_extracted}")

#-------------------
names_to_raw = "0"
names_to_raw = " / ".join(names_extracted)
#you can also get a list back into a string and use a character to 'separate'
#the extracted contents from the list
print(f"Convert separate list back to string, split into slashes: {names_to_raw}")

#-------------------
#unlike regular lists with [], sets {} do have access to intersection/difference
#that has more optimized comparison between two sets with multiple content
#
#take note, to prevent confusion, always use lists and sets should only be used
#if you really need intersection/difference, and is not empty
#to call for an empty set, use set() and never just {} as that involves using dict

setnames_men = {"Casey", "Jonathan", "Markus"}
setnames_women = {"Leila", "Casey", "Jane"}

setnames_bin = setnames_women.intersection(setnames_men)
setnames_women_only = setnames_women.difference(setnames_men)
setnames_all = setnames_women.union(setnames_men)

print(f"List of names of women: {setnames_women}")
print(f"List of names of men: {setnames_men}")
print(f"List of names that apply both to women & men: {setnames_bin}")
print(f"Strictly women names only: {setnames_women_only}")
print(f"All names on both sets: {setnames_all}")