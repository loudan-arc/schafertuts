#also called functions. interchangeable
#much easier to do compared to java or other languages

def hanoi(disc_lvl, start, end, mid):
    if(disc_lvl == 1):
        movedisc(disc_lvl, start, end)
    else:
        hanoi(disc_lvl - 1, start, mid, end)
        movedisc(disc_lvl, start, end)
        hanoi(disc_lvl - 1, mid, end, start)

def movedisc(disc_lvl, start, end):
    print(f"Move disc {disc_lvl} from {start} to {end}")

print("Classic recursion technique to solve the Towers of Hanoi problem: ")
hanoi(3, "A", "C", "B")

#I will be honest. The Hanoi problem has been a challenge for me to understand
#when it comes to how recursion works
#just watch this video for a clear understanding
#https://www.youtube.com/watch?v=rf6uf3jNjbo

#what happens in essence is this, if there are three discs on the tower of hanoi

#first call with 3 discs on left side (3, A, C, B) is put on hold

#second call with 2 discs to be moved from left to center is put on hold. but:
#values change! because the call uses variable (start, mid, end) instead of (start, end, mid)
#when hanoi calls itself, it puts values (a,b,c)
#making hanoi(start=a,end=b,mid=c)

#third call has values change again! Currently what is in it is start=a,end=b,mid=c
#and we're dealing with 1 disc
#remember the inside call uses (start, mid, end)
#when hanoi calls itself, it puts values as (a,c,b)
#making hanoi(start=a,end=c,mid=b)
#which then leads to returning to fulfill IF statement of disc_lvl==1
#and print -- Move disc 1 from A to C

#fourth action, remember the calls for disc_lvl==2 and 3 still are pending
#from SECOND call from disc_lvl==2 earlier can now work, the one where
#hanoi(start=a,end=b,mid=c)
#as it doesn't fulfill if statement it prints the movedisc to
# Move disc 2 from A to B 

#fifth, this is key. The ending hanoi() recursive call also will run both
# disc_lvl==2 and disc_lvl==1

#because the second call with disc_lvl==2 is put on hold
#we continue with the disc_lvl==1 which now has its values
#Move disc 1 from C to B

#it has finished one side of the recursion so we return back to
#FIRST call where disc_lvl==3
#and print Move disc 3 from A to C

#now that's freed up, we can move to the disc_lvl==2 call
#but this time it uses the (mid, end, start scheme)
#meaning the values become
#hanoi(start=B, end=C, mid=A)
#again calls that involve the second won't do anything yet as it will
#go for smallest value on stack
#remember the values again change
#pirint Move disc 1 from B to A

#with that out of the way, 

#def hanoi(disk_lvl, start, end):
#    if(disk_lvl == 1):
#        movedisc(start, end)
#    else:
#        mid = 6-(start+end)
#        hanoi(disk_lvl - 1, start, mid)
#        movedisc(start, end)
#        hanoi(disk_lvl - 1, mid, end)

#def movedisc(start, end):
#    print(f"Move from {start} to {end}")

#hanoi(3, 1, 3)