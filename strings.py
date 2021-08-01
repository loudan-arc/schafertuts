#for i in range(0,101):
#    print(i)

names = ["Hannah", "Anya", "Irina"]

for name in names:
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