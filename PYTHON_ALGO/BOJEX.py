# x_list = []
# y_list = []

# for _ in range(3):
#     x, y = map(int, input().split())
#     x_list.append(x)
#     y_list.append(y)

# for i in range(3):
#     if x_list.count(x_list[i]) == 1:
#         x = x_list[i]
#     if y_list.count(y_list[i]) == 1:
#         y = y_list[i]

# print(x, y)

nums = [00, 1]

n = 6
cnt = 0
target = n//2

for i in range(1, target+1):
    divide = 2*i