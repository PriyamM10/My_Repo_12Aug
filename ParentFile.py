

# How to Import a package ???

"""
import math
import math as mm
from math import sprt, exp
from math import *
"""

# Function 1
# Palindrome Function

def palin( s ) : 
    if s.lower().strip()[ : : 1] == s.lower().strip()[ : : -1] : 
        return 'Palindrome'
    else : 
        return 'Not a Palindrome'
    
# Function 2
## Even Odd Function
even_odd = lambda n : "EVEN" if n % 2 == 0 else "ODD"

# Function 3
# Display Current Time
def WhatsCurrentTime() : 
    import datetime
    timestamp = datetime.datetime.now()
    currentTime = timestamp.strftime("%H : %M")
    return currentTime

# Function 4
# Set Operations

setOps = lambda x, y : f"{x} is superset of {y}" if x.issuperset(y) else ( f"{x} is subset of {y}" if x.issubset(y) else f"No relation" )

