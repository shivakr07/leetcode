class Solution:
    def myAtoi(self, s: str) -> int:
        if s == "":
            return 0
        s = list(s.strip())
        print(s)
        sign = 1
        st = 0
        num = 0
        if s == []:
            return 0
        if s[0] == '-' and s:
            sign = -1
            st = 1
        elif s[0] == '+' and s:
            sign = 1
            st = 1
        
        
        for i in range(st, len(s)):
            if s[i].isdigit():
                num = num*10 + int(s[i]) 
            else:
                print(s[i])
                break
        print(num)
        num = sign * num
        if num >( 2**31 - 1):
            num =  (2**31 - 1)
            print(num)
            return num
        elif num < -(2**31):
            return -2**31
        else:
            return num