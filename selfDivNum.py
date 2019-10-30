def isSelfDiv(num):
    sepNum = list(str(num))
    for i in sepNum:
        if i == '0':
            return False
        if num % int(i) != 0:
            return False
    return True


def main():
    l = 1
    r = 22
    for i in range(l, r+1):
        if isSelfDiv(i):
            print(i)


if __name__ == "__main__":
    main()
