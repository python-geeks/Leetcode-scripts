def ishigher(a,b):
    if a > b:
        print(str(a),"is higher.")
    elif a < b:
        print(str(b),"is higher")
    elif a == b:
        print("Both are equal.")
    else:
        print("Something is fishy.")

# Demo
ishigher(9,8)