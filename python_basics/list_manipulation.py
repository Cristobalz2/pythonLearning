def list(arr, string):
    for i in range (1,4):
        arr[i] = string
    return arr
# print(list(["Isha", "Chandoygya", "Sri Vasya", "Mandukya", "Sri"],"Brahman"))
def doubleList(listA, listB):
    newList = listA + listB
    return newList
A = ['p', 'q', 6, 'k']
B = [8, 10]
# print(doubleList(A, B))

def sortedArray(numberList):
    my_list = numberList[:]
    length = 0
    for element in my_list:
        length = length + 1
    unSorted = True
    while unSorted:
        unSorted = False
        for index in range(0, length-1):
            print(index)
            # if next element is greater element then swap them
            if my_list[index] > my_list[index + 1]:
                temporary_variable = my_list[index]
                my_list[index] = my_list[index + 1]
                my_list[index + 1] = temporary_variable
                unSorted = True
    return my_list
unsortedArray = [ 7, 9, 4, 5, 0, 11]
# print(sortedArray(unsortedArray))

def sortAndReverse(listone, listtwo):
    original_list=listone+listtwo
    my_list = original_list[:]
  
    # get the length of the list
    length = 0
    for element in my_list:
        length = length + 1
    unSorted = True
    while unSorted:
        unSorted = False
        for index in range(0, length-1):
            # if next element is greater element then swap them
            if my_list[index] < my_list[index + 1]:
                temporary_variable = my_list[index]
                my_list[index] = my_list[index + 1]
                my_list[index + 1] = temporary_variable 
                unSorted = True
    return my_list
# print(sortAndReverse(B, unsortedArray))

def oddsum(array):
    for n in array:
        if n % 2 !=0:
            array[array.index(n)] = n + 1
    return array

input_list = [13 , 13, 3, 4, 5, 6]
# print(oddsum(input_list))

def oddSumArray( listA, listB):
    newList = listA + listB
    oddsum = 0
    for index in range(len(newList)):
        if newList[index] % 2 != 0:
            oddsum += newList[index]
    return oddsum

# print(oddSumArray(unsortedArray, B))

def uniqueArray(listA):
    output_list = []
    for items in listA:
        if items not in output_list:
            output_list.append(items)
    return output_list
# print(uniqueArray([1, 2, 3, 4, 5, 6, 6]))                






