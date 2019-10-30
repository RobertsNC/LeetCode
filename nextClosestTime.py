def nextClosest(time):
    hour = time[:2]
    min = time[3:]
    print(hour, min)
    digits = list(time[:])


def main():
    input = ["19:34", "12:12", "18:10"]
    for time in input:
        nextClosest(time)


if __name__ == '__main__':
    main()
