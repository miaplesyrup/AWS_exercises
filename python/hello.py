# def say_my_type(value):
#     # print(str(121.45) + " is of data type " + str(type(121.45)))
#     print(f"{str(value)} is of data type {str(type(value))}")

# fruits = ["Apple", "Orange", "Grapes"]

# for fruit in fruits:
#     say_my_type(fruit)

# for fruit in fruits[1:]:
#     say_my_type(fruit)

# say_my_type(121.45)

# for index, fruit in fruits.items():
#     print(index + " " + fruit)








sum = 0

for i in range(1000):
    if (i%3 == 0 or i%5 == 0):
        print(i)
        sum += i

print(sum)


