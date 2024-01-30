q = int(input())
commands = []
for i in range(q):
    commands.append(list(map(int, input().split())))
sequence = []

for cmd, pos, value in commands:
    if cmd == 1:  # insert
        if pos == 0:
            sequence.insert(0, value)
        else:
            sequence.append(value)

    elif cmd == 2:  # erase
        count = 0
        if pos == 0:
            for i in range(len(sequence)):
                if sequence[i] >= value:
                    sequence[i] = None
                    count += 1
                    if count == 3:
                        break
            sequence = [x for x in sequence if x is not None]
        else:
            for i in range(len(sequence)-1, -1, -1):
                if sequence[i] >= value:
                    sequence[i] = None
                    count += 1
                    if count == 3:
                        break
            sequence = [x for x in sequence if x is not None]

    elif cmd == 3:  # sort
        sequence.sort(key=lambda x: (abs(x - value), x))

    elif cmd == 4:  # print
        if pos == 0:
            print(" ".join(map(str, sequence)))
        else:
            print(" ".join(map(str, sequence[::-1])))