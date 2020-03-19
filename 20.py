curr_rep_len = 0
max_len = 1
prev = int(input())
element = int(input())
while element != 0:
    if element > prev:
        curr_rep_len += 1
        prev = element
    elif element == prev:
        curr_rep_len += 0
    else:
        if curr_rep_len == 0 or curr_rep_len < max_len:
            continue
        else:
            max_len = curr_rep_len
            curr_rep_len = 0
    element = int(input())
if max_len > curr_rep_len:
    print(max_len)
elif curr_rep_len > max_len:
    print(curr_rep_len + 1)
