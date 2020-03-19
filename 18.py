k = int(input())
palindrome_counter = 0
i = 1
while i <= k:
    str_i = str(i)
    rev_i = "".join(reversed(str_i))
    if str_i == rev_i:
        palindrome_counter += 1
    i += 1
print(palindrome_counter)
