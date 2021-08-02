import sys
sys.path.append("C:\\Apps\Python\\Python38\\python_tuts\\mods")
#sets environment variable path to include our mods folder
#sys represents system library

import useless_mod as us
#vscode has an error only due to it not being set to see
#but it will actually work
#the scope for useless_mod
#imports the useless_mod.py from the mods folder

us.read_paths()
#invokes the read_paths() function from useless_mod.py
#prints all the available environment variable paths
#which now indeed include mods folder