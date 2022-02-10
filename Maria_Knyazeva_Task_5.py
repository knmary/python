import copy
import operator

list_main = [77.09,12,87.1,55.55,7.4,8.11,23.65,34,5,8.6,111.67,234.8]
print("Part B : ",id(list_main))
part_a=[]
for x in list_main:
    _list = str(x).split(".")
    if len(_list) == 1:
        _list.append("00")
        x = int(round(x))
        list_main.sort()
        list_c = sorted(list_main, reverse=True)

    num_a = f'{str(_list[0])} руб {int(_list[-1]):02d} коп'
    part_a.append(num_a)

print("Part A : ",", ".join(part_a))
print("Part B : ", list_main)
print("Part B : ",id(list_main))
print("Part C : ",list_c)
print("Part D : ",list_c[0:5])
print("Part D : ",sorted(list_c[0:5],reverse=False))

















    # for y in list_2:
    #     if list_2[y] < 1:
    #         list_2.append(00)

    #num1 = str(x).split(".")
   # str(x).split(".").pop(-1)__ #дает первый элемент
    #num1.pop(0) #дает последний элемент





