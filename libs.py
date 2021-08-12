import random as rnd
import datetime as dt
import math as mt
import os

soldiers = ["Medic", "Engineer", "Bomber", "Scout"]

rnd_type = []

for f in range(0, 10):
    rnd_type.append(rnd.choice(soldiers))
    #choice() is basically the equivalent of rand in other languages

print(f"Invoked random soldier type from the list 10 times on {dt.datetime.now()}")
#equivalent for datetime.now
print(rnd_type) #printing the array that received 10 appended random stuff

pi = mt.pi
pi_round_up = mt.ceil(pi)
pi_round_down = mt.floor(pi)

print(f"Pi = {pi}")
print(f"Pi rounded up = {pi_round_up}")
print(f"Pi rounded down = {pi_round_down}")