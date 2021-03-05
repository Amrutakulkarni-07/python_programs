# Accept N Numbers from users
# anfter  that filter out even number from that number
# and 2 to that every number

# input[1,3,2,4,6,5,4]
# After  filter[2,4,6,4]
# After map[4,6,8,6]
# After reduce 24

import functools

def main():
    arr = []
    print("Enter the number of elemets")
    size = int(input())

    for i in range(size):
        print("Enter element number:", i + 1)
        no = int(input())
        arr.append(no)

    print("Your enter elements are", arr)

    print(functools.reduce(lambda no1, no2: no1 + no2,list(map(lambda no: no + 2, list(filter(lambda no: (no % 2 == 0), arr))))))

if __name__ == "__main__":
    main()