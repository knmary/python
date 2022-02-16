def thesaurus(*names):
    names_get = {name.title() for name in names}
    first_letter = [name[0].upper() for name in names_get]
    result_dict = {k: list() for k in first_letter}

    for name in names_get:
        result_dict[name[0]].append(name)

    return result_dict

print(thesaurus("Мария", "Иван", "Максим", "Петр"))
