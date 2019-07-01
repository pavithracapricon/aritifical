import sys  
def isKthBitSet(x, k): 
    if ((x & (1 << (k - 1))) !=0): 
      return True
    else: 
      return False
  
def is Palindrome(x): 
    l = 1 # Initialize left position 
    r = 2 * 8 # initialize right position 
  
    
    while (l < r): 
        if (isKthBitSet(x, l) != isKthBitSet(x, r)): 
            return False
        l += 1
        r -= 1
      
    return True
