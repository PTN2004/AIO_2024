def calc_f1_score(tp, fp, fn):

    if not isinstance(tp, int):
        print('Error: tp must be int')
        return

    if not isinstance(fp, int):
        print('Error: fp must be int')
        return

    if not isinstance(fn, int):
        print('Error: fn must be int')
        return

    if tp == 0 or fn == 0 or fp == 0:
        print('Error: tp and fp and fn must be greater than zero')
        return

    precition = tp/(tp+fp)
    print('precition is ', precition)

    recall = tp/(tp+fn)
    print('recall is ', recall)

    f1_score = 2*((precition * recall) / (precition + recall))
    print('f1_score is ', f1_score)


print("---------")
calc_f1_score(2, 3, 4)

print("---------")
calc_f1_score(99, 100, 20)

print("---------")
calc_f1_score(0, 3, 4)

print("---------")
calc_f1_score(1, 0, 5)

print("---------")
calc_f1_score(6, 3, 0)

print("---------")
calc_f1_score('a', 5, 4)

print("---------")
calc_f1_score(2, 'b', 1)

print("---------")
calc_f1_score(2, 4, 'c')
