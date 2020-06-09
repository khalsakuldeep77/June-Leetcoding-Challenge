class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n <= 0:
            return False    
        
        # note:
        # power of 2 in binary         = b' 1000 ... 0
        # power of 2 minus 1 in binary = b' 0111 ... 1
        # bitwise AND of n and (n-1) must be 0 if n is power of 2
        
        return ( n & ( n-1 ) ) == 0