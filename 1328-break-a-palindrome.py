def breakPalindrome(palindrome):
    if len(palindrome) == 1:
        return ""
    palindrome = list(palindrome) 
    i =  0
    j = len(palindrome)-1

    while i <= j:
        if palindrome[i] == 'a' and palindrome[j] == 'a':
            i += 1
            j -= 1
            continue
        elif palindrome[i] == palindrome[j]:
            palindrome[i] = 'a'
            break
        else:
            palindrome[j] = 'a'
            j -= 1
            i -= 1
    return palindrome


st = "aba"
ans = breakPalindrome(st)
print(ans)