#######################
## EXAMPLE: returning a tuple
#######################
def quotient_and_reminder(x,y):
    q = x // y
    r = x % y 
    return (q, r)

(quot, rem) = quotient_and_reminder(5,3)
print(quot)
print(rem)
