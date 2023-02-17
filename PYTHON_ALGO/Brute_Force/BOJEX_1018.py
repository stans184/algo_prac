# context = "55-50+40+40"
# num_list = []

# print(context.find("+"))
# print(context.find("-"))
# print(context.find("+"))

expression = input().split('-')  # split by '-'
result = sum(map(int, expression[0].split('+')))  # calculate the first part before '-'
for e in expression[1:]:
    result -= sum(map(int, e.split('+')))  # subtract the remaining parts after '-'
print(result)