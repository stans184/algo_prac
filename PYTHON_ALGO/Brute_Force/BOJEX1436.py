n = int(input()) # number of people

# create a list of tuples to store each person's weight and height
people = []
for i in range(n):
    w, h = map(int, input().split())
    people.append((w, h))

# compare each person's weight and height with every other person
rank = [1] * n # initialize the rank of each person to 1
for i in range(n):
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank[i] += 1

# print the rank of each person
for r in rank:
    print(r, end=' ')