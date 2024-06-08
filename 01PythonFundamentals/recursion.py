# recursion problems from my discrete math hw this week 

def Fib(n): 
    if n <= 0:
        return 0
    elif n ==1:
        return 1
    else:
        return Fib(n - 1) + Fib(n - 2)
    
print("fibonacci of 4 is:", Fib(4))


def S(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 2
    else: 
        return S(n-1)**2
print("S(4) is:", S(4))


# read more on: why does seq need to be defined as none in the header first?
# kinda skipped ahead a bit and wrote these before i actually learned about lists
recList = None
def recaman(n, seq = None):
    global recList
    if seq is None:
        seq = [0]
    
    if n == 1:
        if 1 not in seq:
            seq.append(1)

        return 1
    else:
        prev = recaman(n-1, seq)
        newRec = prev - n
        
        if newRec <= 0 or newRec in seq:
            newRec = prev + n
        
        seq.append(newRec)
        recList = seq.copy()
        return newRec
recaman(10)
print("first 10 numbers of Recaman's sequence are:\n", recList)



