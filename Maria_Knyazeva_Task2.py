number_list = []
sum = 0
for n in range(1,1001):
    if n % 2 != 0:
        number_list.append(n ** 3)
for idx in range(len(number_list)):
    numb_count = 0
    q = number_list[idx]
    while q:
        numb_count += q % 10
        q = q // 10
    if numb_count % 7 == 0:
        sum += number_list[idx]

print(sum)



































