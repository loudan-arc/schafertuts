print("enum_mod loaded")

def seek_instance(info, seek):
    for key, val in enumerate(info):
        if val == seek:
            return key
    return -1
#this will read two items
#info = a list of items it will get index and values from
#seek = an item it'll try to compare from a list if it exists
#in this case this will be used to compare strings, but numbers
#should also work

def remove_instance(info, seek_del):
    for key, val in enumerate(info):
        if val == seek_del:
            info.pop(key)
            return key
    return -1
#info is meant to read a list, this is key
#with a list you can invoke .pop() <-- see lists.py
#but here you use .pop(key) so you can pop off a specific item index
#so it's not confined to removing last item