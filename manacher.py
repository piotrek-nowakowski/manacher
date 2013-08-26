"""
Python implementation of Manacher's algorithm, which allows to find longest 
palindromic substring as well as number of palindromic substrings in a string.
Time complexity: O(N) <-- cool
Space complexity: O(N)
"""

def get_palindrome_length(string, index):
    """
    Returns length of longest palindromic substring centered in the given index. 
    """
    length = 1
    while index + length < len(string) and index - length >= 0:
        if string[index + length] == string[index - length]:
            length += 1
        else:
            break
        
    return length - 1


def interleave(string):
    """
    Returns a interleaved version of a given string. 'aaa' --> '#a#a#a#'.
    Thanks to thin function we don't have to deal with even/odd palindrome 
    length problem.
    """
    ret = []
    for s in string:
        ret.extend(['#', s])
    ret.append('#')
    
    return ''.join(ret)


def manacher(string):
    """
    Computes length of the longest palindromic substring centered on each char 
    in the given string. The idea behind this algorithm is to reuse previously 
    computed values whenever possible (palindromes are symmetric).
    
    Example (interleaved string):
    i    0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 
    s    #  a  #  b  #  c  #  q  #  q  #  q  #  q  #  q  #  q  #  x  #  y  #
    P    0  1  0  1  0  1  0  1  2  3  4  5  6  5  4  ?
                                    ^        ^        ^        ^
                                  mirror   center   current  right
    
    We're at index 15 wondering shall we compute (costly) or reuse. The mirror
    value for 15 is 9 (center is in 12). P[mirror] = 3 which means a palindrome
    of length 3 is centered at this index. A palindrome of same length would be
    placed in index 15, if 15 + 3 <= 18 (right border of large parlindrome 
    centered in 12). This condition is satisfied, so we can reuse value from
    index 9 and avoid costly computation.
    """
    right = 0
    center = 0
    string = interleave(string)
    P = map(lambda e: 0, xrange(len(string)))
    
    for i in xrange(1, len(string)):
        mirror = 2*center - i
        if i + P[mirror] <= right and mirror >= len(string) - i:
            P[i] = P[mirror]
        else:
            plength = get_palindrome_length(string, i)
            P[i] = plength
            if plength > 1:
                center = int(i)
                right = center + plength
    
    return [e/2 for e in P]


def get_palindrome_number(string):
    return sum(manacher(string))