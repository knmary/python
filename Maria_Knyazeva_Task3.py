number_N = 1
while number_N <= 100:
    _number_N = str(number_N)
    if len(_number_N) >= 1:
        if _number_N[-1] == "5" or _number_N[-1] == "6" or _number_N[-1] == "7" or _number_N[-1] == "8" or _number_N[-1] == "9" or _number_N[-1] == "0" or number_N == 11 or number_N == 12 or number_N == 13 or number_N == 14:
            print(number_N,"процентов")
        elif   _number_N[-1] == "2" or _number_N[-1] == "3" or _number_N[-1] == "4":
            print(number_N, "процента")
        else:
            print(number_N, "процент")
    number_N += 1






