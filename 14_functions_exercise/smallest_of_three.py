def smallest_of_three(n_1, n_2, n_3):
    result = n_1
    if n_2 < result:
        result = n_2
    if n_3 < result:
        result = n_3
    return result

number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
print(smallest_of_three(number_1, number_2, number_3))