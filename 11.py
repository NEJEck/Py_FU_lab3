prev = int(input())
answer = 0
while prev != 0:
    next_num = int(input())
    if next_num != 0 and prev < next_num:
        answer += 1
    prev = next_num
print(answer)
