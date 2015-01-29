__author__ = 'existentialtype'

class Solution:
    # @return an integer
    def powers_of_five(self):
        count=1
        while True:
            yield pow(5,count)
            count+=1

    def trailingZeroes(self, n):
        sum=0
        gen_powers=self.powers_of_five()
        for m in gen_powers:
            if (m<=n):
                sum+=n//m
            else:
                break
        return sum
