from threading import Thread

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

def Make_Dir(lst_Partitions):
    l2=[]
    for i in lst_Partitions:
        s=''
        for j in i:
            s+= str(j)+'+'
        l2.append(s[:len(s)-1])
    u=''
    for k in l2:
        u+=k+'\n'
    print ('Starting to write')
    open('Partitions Of- '+str(sum(lst_Partitions[0]))+'.txt','a').write(u)
    print ('Completed '+str(sum(lst_Partitions[0])))

def Create_and_Save_Parts(s):
    Make_Dir((Partitions(s)))

def main():
    int_Starting=int(input("Enter the starting Number: "))
    int_Last=int(input("Enter the Last Number: "))
    if int_Starting>int_Last:
        raise ValueError("The Starting Number is greater than the Last Number")
    for Number in range(int_Starting,int_Last+1):
        print(Number)
        try:
            Thread(target = Create_and_Save_Parts, args = (Number,)).run()
        except Exception as Error:
            open('Reasons Why This Failed.txt','w').write(Error.message)

if __name__ == '__main__':
    main()
