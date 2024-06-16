def sort_chars_in_dictionary(dictionary):
    list_key = [key for key in dictionary]
    list_key.sort()

    result = {i: dictionary[i] for i in list_key}

    return result


def count_chars(string):

    if not isinstance(string, str):
        print("The type of string must be 'str' type")
        return None

    string = str(string).strip()
    len_string = len(string)
    if string.isnumeric():
        print('String in range [a-z] or [A-Z]')
        return None

    if len_string == 0:
        print('The lenght of the string must be greater than one charecter!')
        return None

    result = {}
    for i in range(len_string):
        count = string.count(string[i])
        result.setdefault(string[i], count)

    return sort_chars_in_dictionary(result)


test1 = "Happiness"
print(count_chars(test1))

test2 = ""
print(count_chars(test2))

test3 = "I LOVE AI VIETNAM"
print(count_chars(test3))

test4 = "122345"
print(test4.isnumeric())

test5 = 123
print(count_chars(test5))
