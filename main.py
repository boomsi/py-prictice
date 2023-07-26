# arr = [3, 6, 2, 7]

# res = []

# for i in arr:
#     for j in arr:
#         if i == j:
#             continue
#         for z in arr:
#             if i == z or j == z:
#                 continue
#             res.append(i * 100 + j * 10 + z)

# print(res, len(res))



# lst_1 = [1, 2, 3, 4]
# lst_2 = ['a', 'b', 'c', 'd']

# res = []

# for i in lst_2:
#     res.append([])
#     for j in lst_1:
#         res[-1].append(str(j) + str(i))


# print(res)


# lst = [1,2,3,4,5]，列表向右偏移两位后，变成lst = [5,4,1,2,3]

lst = [1,2,3,4,5]

def move(lst: list, n):
    nn = len(lst) - n
    mid = list(reversed(lst[nn:]))
    nlst = lst[:nn]
    return mid + nlst

print(move(lst, 2))
