# https://leetcode.com/problems/reorder-data-in-log-files/

def reorderLogFiles(logs:list[str]) -> list[str]:
    letters, digits = [], []
    for log in logs:
        print(log.split())
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    print(letters)
    print(digits)    
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits

print(reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))
