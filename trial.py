class Solution:
    def isPalindrome(self, x: int) -> bool:
        lst=list()
        sum=0
        cp=abs(x)

        while cp>0:
            lst.append(cp%10)
            cp=int(cp/10)
        
        for i in range(len(lst)):
            lst[i]=lst[i]*10**(len(lst)-1-i)
            sum+=lst[i]
            
        return sum==x


class Solution:
    def isPalindrome(self, x: int) -> bool:
        cp=x
        lst=list()

        while cp>0:
            lst.append(cp%10)
            cp//=10

        res=[val*10**(len(lst)-1-i) for i, val in enumerate(lst)]
        return sum(res)==x

class Solution:
    def is_palindrome(n):
        cp = abs(n)
        lst = []

        while cp > 0:
            lst.append(cp % 10)
            cp //= 10

        res = [val * 10**(len(lst) - 1 - i) for i, val in enumerate(lst)]
        return sum(res)
