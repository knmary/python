"""Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:

Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации."""

SRC = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

spk_copy = set()
spk_1 = set()
s = []
for src_name in SRC:
    if src_name in spk_copy:
        continue
    if src_name in spk_1:
        spk_copy.add(src_name)
        spk_1.discard(src_name)
        continue
    spk_1.add(src_name)
print(spk_1)

