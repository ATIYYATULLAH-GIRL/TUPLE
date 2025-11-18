def pal(r):
    ending=len(r)-1
    starting=0
    while starting<ending:
        if r[starting]!=r[ending]:
            return False
        starting+=1
        ending-=1
    return True
r=(1,2,3,4,3,2,1)
if (pal(r)):
    print("It is a palindrome")
else:
    print("It is not a palindrome")