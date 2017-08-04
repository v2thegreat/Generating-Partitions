def Partitions(n):
    partitions_of = []
    partitions_of.append([()])
    partitions_of.append([(1,)])
    for num in range(2, n+1):
        ptitions = set()
        for i in range(num):
            for partition in partitions_of[i]:
                ptitions.add(tuple(sorted((num - i, ) + partition)))
        partitions_of.append(list(ptitions))
    return partitions_of[n]

def main():
    int_Part_Number = int(input("Enter the Number: "))
    for x in Partitions(int_Part_Number):
        print(x)

if __name__ == '__main__':
    main()