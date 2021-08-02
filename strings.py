#for i in range(0,101):
#    print(i)

ctr = 0
names = ["Hannah", "Anya", "Irina", "Olivia"]

for name in names:
    print()
    print(f"Full name: {name}")
    #using f inside print allows using variables inside string held by braces

    print("first three chars: " + name[0:3])
    #since Strings are in a way char lists, you can only specify which chars to print
    #0 can be replaced by any number for starting index
    #3 can be replaced by any number for total range of numbers. NOT ending index
    #so the output is the first three characters which technically is name[0] up to name[2]
    
    print("first two chars caps: {}".format(name[0:2].upper()))
    #aside from using printf, using format is applicable, braces inside string
    #is replaced by whatever is in format

    print("first four chars lowercase: {}".format(name[0:4].lower()))

    print(f"Number of times letter A appears on name: {name.count('a')}")
    #be aware that when using strings, you can either use " " or ' ' but
    #ensure to add backslash to literally print the symbols

print("\nGetting names list..")
while ctr < 4: #tries to loop through for items of an array
    if names[ctr] == "Olivia": #if it finds names[3]
        print("Skipping fourth name..")
        break #loop breaks and does not continue any further, skipping name
    print(names[ctr])
    ctr += 1
#python has no do while, just while so it's best to set a counter
#or any other statement that eventually gets fulfilled

print("\nRe-acquiring names list..")
for f in range(0, 4):
    print(names[f])
#while other programming languages use for(f==0; f<4; f++)
#python just uses range(0,4)
#so 0 is the starting index, 4 is like f<4 so it doesn't include 4 on
#the actual loop, the number before it
#so it prints all names from names[0] to names[3]
