
def main():
    startArray = [7, 12, 19, 3, 18, 4, 2, 6, 15, 8]
    firstHalf = startArray[:len(startArray)//2]
    secondHalf = startArray[len(startArray)//2:len(startArray)]
    n1 = len(firstHalf)
    n2 = len(secondHalf)
    firstHalf.sort()
    secondHalf.sort()
    i, j, k = 0, 0, 0
    final = []

    while i < n1 and j < n2:
        if firstHalf[i] < secondHalf[j]:
            final.append(firstHalf[i])
            i += 1
        else:
            final.append(secondHalf[j])
            j += 1

    while i < n1:
        final.append(firstHalf[i])
        i += 1
    while j < n1:
        final.append(secondHalf[j])
        j += 1

    print(final)


if __name__ == "__main__":
    main()
