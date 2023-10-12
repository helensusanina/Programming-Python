str = [x for x in input().split()]
print("True" if len(str) == len(set(str)) else "False")
