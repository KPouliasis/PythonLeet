__author__ = 'existentialtype'
import functools
class Solution:
    # @param num, a list of integers
    # @return a string

    def largestNumber(self, num):

        def mycomp(a,b):
            return int(a+b)-int(b+a)
        #to_strings=list(map(str,num)) for python 3
        to_strings=list(map(str,num))
        to_strings.sort(key=functools.cmp_to_key(mycomp),reverse=True)
        res=""
        for el in to_strings:
            res+=el
        while (res[0]=='0') and (res[1:]):
            res=res[1:]
        return res
