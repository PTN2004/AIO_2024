def create_matrix(m, n):
    return [[0 for _ in range(n + 1)] for _ in range(m + 1)]


def levenshtein_distance(source, target):
    len_source = len(source)
    len_target = len(target)

    matrix = create_matrix(len_source, len_target)

    for i in range(len(matrix[0])):
        matrix[0][i] = i
    for i in range(len(matrix)):
        matrix[i][0] = i

    for i in range(1, len_source + 1):
        for j in range(1, len_target + 1):
            if source[i-1] == target[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                dele = matrix[i-1][j] + 1
                ins = matrix[i][j-1] + 1
                rep = matrix[i-1][j-1] + 1
                matrix[i][j] = min(dele, ins, rep)

    return matrix[len_source][len_target]


str1 = 'yu'
str2 = 'you'
distance = levenshtein_distance(str1, str2)
print(f'Lenvenshtein distance ({str1} -> {str2}): {distance}')

str3 = 'kitten'
str4 = 'sitting'
distance = levenshtein_distance(str3, str4)
print(f'Lenvenshtein distance ({str3} -> {str4}): {distance}')

str5 = 'hi'
str6 = 'hello'
distance = levenshtein_distance(str5, str6)
print(f'Lenvenshtein distance ({str5} -> {str6}): {distance}')

str7 = 'hola'
str8 = 'hello'
distance = levenshtein_distance(str7, str8)
print(f'Lenvenshtein distance ({str7} -> {str8}): {distance}')
