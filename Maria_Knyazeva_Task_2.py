def get_sign(x):
    if x[0] in '+-':
        return x[0]

arr_main = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(arr_main))

i = 0
while i < len(arr_main):
    sign = get_sign(arr_main[i])
    if arr_main[i].isdigit() or (sign and arr_main[i][1:].isdigit()):
        if sign:
            arr_main[i] = sign + arr_main[i][1:].zfill(2)
        else:
            arr_main[i] = arr_main[i].zfill(2)

        arr_main.insert(i, '"')
        arr_main.insert(i + 2, '"')
        i += 2

    i += 1

print(arr_main)
print(" ".join(arr_main))
print(id(arr_main))