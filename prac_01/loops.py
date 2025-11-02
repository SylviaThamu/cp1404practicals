def main():
    # a. count in 10s from 0 to 100
    print("a.")
    for number in range(0, 101, 10):  # start=0, stop=101 (so it includes 100), step=10
        print(number, end=" ")
    print()  # move to the next line

    # b. count down from 20 to 1
    print("b.")
    for number in range(20, 0, -1):  # start=20, stop=0 (so it includes 1), step=-1
        print(number, end=" ")
    print()

    # c. print a number of stars on one line
    print("c.")
    number_of_stars = int(input("Number of stars: "))
    for count in range(number_of_stars):  # repeat as many times as number_of_stars
        print("*", end="")
    print()  # move to the next line after all stars are printed

    # d. print lines of increasing stars
    print("d.")
    number_of_lines = int(input("Number of lines: "))
    for line in range(1, number_of_lines + 1):  # start at 1, go up to number_of_lines
        print("*" * line)  # repeat "*" line times


main()
