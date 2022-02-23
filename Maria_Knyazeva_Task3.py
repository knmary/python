
TUTORS = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
KLASSES = [
    '9А', '7В', '9Б', '9В', '8Б', '10А','10Б', '9А'
]

def tuple_pair(TUTORS,KLASSES):
    x = len(TUTORS) - len(KLASSES)
    if x > 0:
        for _x in range(x):
           KLASSES.append(None)
    for itm1, itm2 in zip(TUTORS,KLASSES):
        yield itm1,itm2

r = tuple_pair(TUTORS,KLASSES)
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
