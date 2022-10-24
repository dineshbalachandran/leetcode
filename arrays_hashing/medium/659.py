"""
Medium

659. Encode and decode strings

Description
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode


Example

Example1
Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"
Example2

Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"


"""

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        return ''.join([str(len(s))+"#"+s for s in strs])            


    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, strs):
        # write your code here
        e, l = -1, 0
        
        res = []
        while True:
            f = e+l+1
            e = strs.find('#', f)
            if e == -1:
                break            
            l = int(strs[f:e])
            s = strs[e+1:e+l+1]
            res.append(s)

        return res

if __name__ == "__main__":

    tests = [   
        ["lint","code","love","you"],
        ['we', 'say', '#', "yes"]
    ]

    for test in tests:
      s = Solution().encode(test)
      print(Solution().decode(s))