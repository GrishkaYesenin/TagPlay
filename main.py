CONFIG = (3, 4, 5)


def make_snake_seq(arr2d):
    res = []
    for i, line in enumerate(arr2d):
        if i % 2 == 0:
            res += line
        else:
            res += line[::-1]
    print(res)
    res.remove(0)
    return res


def make_original_snake_seq(n):
    arr = [[n*i+j for j in range(1, n+1)] for i in range(n)]
    return make_snake_seq(arr)


def count_wrong_couples(arr):
    counter = 0
    for i, elem in enumerate(arr):
        for second_elem in arr[i+1:]:
            if elem > second_elem:
                counter += 1
    return counter


def make_decision(n, arr):
    origin_arr = make_original_snake_seq(n)
    size = n**2-1
    # print(origin_arr)
    # print(arr)
    i = 0
    while i < size:
        if arr[i] != origin_arr[i]:
            # print(arr[i:], origin_arr[i:])
            # print(count_wrong_couples(origin_arr[i:]), count_wrong_couples(arr[i:]))
            # make slices origin_arr[i:] and arr[i:]
            if count_wrong_couples(origin_arr[i:]) - count_wrong_couples(arr[i:]) % 2 == 0:
                return 'True'
            else:
                return 'False'
        i += 1
    return 'Trueeeeeeeeeeeee'

n = int(input())

arr2d = [list(map(int, input().split())) for i in range(n)]

arr = make_snake_seq(arr2d)

decision = make_decision(n, arr)
print(decision)