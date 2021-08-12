import os, re

mkv_command = ""
gimp_counter = 0
loc = "C:\\Users\\AutotrophLane\\Pictures\\Games\\"
files = os.listdir(loc)
files_found = list()
# First, we set the location for the directory on where the files must be found from.
# We put that into os.listdir(loc)

files_list = "\n".join(files)
# While we can iterate through the files list as is and regex that way, it's
# kind of more efficient to put it all in a single string and newline from there
# for each item

gimp_regex = re.compile(r".*\.xcf")
# the actual Regex pattern to be used to parse which files should be found or not

#for filename in files:
#    print(filename)
#   files_found.append(gimp_regex.findall(filename))

gimp_found = gimp_regex.findall(files_list)
# Uses gimp_regex Regex pattern and finds all information within the String
# in which items fit the pattern. For items that fit the pattern it is put into
# a list

for gimp_find in gimp_found:
    gimp_counter += 1
    #print("{}: {}".format(gimp_counter, gimp_find)) <-- format works but is dated
    print(f"{gimp_counter}: {gimp_find}")
# iterate through that list and print it all and format appropriately