import sys


def check_k(k):
    return k >= 1


def list_max_in_sliding(num_list, k):
    size_list = len(num_list)
    if not check_k(k):
        print("K must be greater than or equal to one !")
        return None

    if size_list == 0:
        print("ERROR:List is empty")
        return None

    if k == 1:
        return num_list

    if k > size_list:
        print(f"ERROR: k must be less than or equal {size_list}")
        return None

    result = []

    for index in range(size_list):
        maximun = num_list[index]

        for j in range(index + 1, k):
            maximun = max(maximun, num_list[j])

        result.append(maximun)
        k += 1
        if not check_k(k) or (k > size_list):
            break

    return result


num_list1 = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k1 = 3
print(list_max_in_sliding(num_list1, k1))

num_list2 = [2, 4, 5, 3, -12, 6, 9, 10]
k2 = 1
print(list_max_in_sliding(num_list2, k2))

num_list3 = [5, 5, 5, 5, 5, 5, 5]
k3 = 4
print(list_max_in_sliding(num_list3, k3))

num_list4 = [5, 2, -1, 0, 1, 9, 100, 20]
k4 = 9
print(list_max_in_sliding(num_list4, k4))

num_list5 = []
k5 = 3
print(list_max_in_sliding(num_list5, k5))
