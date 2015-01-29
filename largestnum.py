__author__ = 'existentialtype'
class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):

        def mycomp(a,b):
            return cmp(int(a+b),int(b+a))
        to_strings=map(str,num)
        to_strings.sort(mycomp,reverse=True)
        res=""
        for el in to_strings:
            res+=el
        while (res[0]=='0') and (res[1:]):
            res=res[1:]
        return res
