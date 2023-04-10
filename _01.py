array = [5,4,7,1,9,6,3]
sum=int(input("ENTER THE SUM : "))
print("array = ",array)

def find(array, len, sum):
    print("Pairs whose sum is : ", sum)
    for i in range(len):
        for j in range(i, len):
            if (array[i] + array[j]) == sum:
                print(array[i], array[j])

find(array, len(array), sum)
