duration = int(input("Введите число:"))
if duration < 60:
        print (duration,"сек")
else:
    if duration < 3600:
        min = duration // 60
        sec = duration - min * 60
        print(duration // 60, "мин", sec, "сек")
    else:
        if duration < 86400:
            hour = duration // 3600
            min = (duration - hour * 3600) // 60
            sec = duration - hour * 3600 - min * 60
            print(hour, "ч", min, "мин", sec, "сек")
        else:
            day = duration // 86400
            hour = (duration - day * 86400) // 3600
            min = (duration - day * 86400 - hour * 3600) // 60
            sec = duration - day * 86400 - hour * 3600 - min * 60
            print(day, "д", hour, "ч", min, "мин", sec, "сек")


