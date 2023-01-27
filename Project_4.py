a = 0
total_length = 0

while a <= 10000:
    import random

    x = (random.randint(1,6))
    myList = []

    while x != 6:
        myList.append(x)
        x = (random.randint(1,6))

    myList.append(6)
    print(myList)
    total_length = total_length + len(myList)
    a = a + 1

average = total_length/a
print(average)