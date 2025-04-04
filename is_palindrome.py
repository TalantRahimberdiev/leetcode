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

def roman_to_int(roman):
    dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    converted = [dict[symbol] for symbol in roman]

    to_be_kept=converted.copy()
    i = 0
    while i < len(to_be_kept) - 1:
        if to_be_kept[i] < to_be_kept[i + 1]:
            to_be_kept[i] = 0
            to_be_kept[i + 1] = 0
            i += 2
        else:
            i += 1

    to_be_subtracted=list()
    for j in range(len(converted)-1):
        if converted[j] < converted[j+1]:
            to_be_subtracted.append(converted[j+1]-converted[j])

    return sum(to_be_kept)+sum(to_be_subtracted)


print(roman_to_int('MCMXCVI'))


class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        total = 0
        prev = 0

        for char in reversed(s):
            value = roman[char]
            if value < prev:
                total -= value
            else:
                total += value
                prev = value

        return total
