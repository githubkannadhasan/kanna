

def ListinEven(list1):
    list2 =[]
    for i in list1:
        if i%2 ==0:
            list2.append(i)
    print(list2)


list1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

ListinEven(list1)

