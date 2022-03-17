print("Hello World")
print("abc")

# input making programming dynamic
# username = input("Your Name:")
# print(f"Hello{username}!!")
# print("Hello".format(username))-> Another Way(Old Version)

#Functions
def add_two_values(first,second):
    return first + second

number_1 = 10
number_2 = 20
sum = add_two_values(number_1, number_2)

print(f"{number_1} + {number_2} = {sum}")
#print(f"Sum={sum}")


print("1")
def complicated_logic(first,second):
    print(f"You Passed:{first}, {second}")

number_1 = 10
number_2 = 20
print("2")
complicated_logic(number_1, number_2)
complicated_logic(3,4)
print("3")

#Data Types
first_value = 40
second_value = 4

addition = first_value + second_value
subtraction = first_value - second_value
multiply = first_value * second_value
division = first_value/second_value
multiply2 = first_value * 3
division2 = first_value / 5
division2_int = first_value // 5
remainder = first_value % 5

print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiply}")
print(f"Division: {division}")
print(f"Multiplication2: {multiply2}")
print(f"Division2: {division2}")
print(f"Division2_Int: {division2_int}")
print(f"Remainder: {remainder}")

person_name = "Ashfat Abegh"
food = "burger"
value2 = 10
Ashfat_Abegh_With_Number = person_name + " " + str(value2)
concateneted_string = Ashfat_Abegh_With_Number + " " + food
print(concateneted_string)
print(f"Length of Name: {len(Ashfat_Abegh_With_Number)}")

#List
grocery_list = ["potato", "tomato", "rice"]
grocery_list.append("water")
grocery_list.sort() #Sorting
l2 = list()
l2.append(4)
l2.append("Computer")

print(l2)
print(grocery_list)
second_item = grocery_list[1]
print(f"Second Item: {second_item}")
print(grocery_list[-2]) #for last item[-1,-2]

numbers = [1, 70, 5, 3, 40, 76]
sorted_list = sorted(numbers)
print(f"Numbers: {numbers}")
print(f"Sorted List: {sorted_list}")

#Condition
#marks = int(input("What is your marks in programming?:"))

# def show_grade(grade):
#     print(f"You got: {grade}")
#
# #use of and
# if marks >  80:
#     show_grade("A+")
# elif marks == 80:
#     show_grade("A")
# elif marks < 80 and marks >= 70:
#     show_grade("A")
# elif marks < 70 and marks >= 60:
#     show_grade("A-")
# elif marks == 33:
#     show_grade("B")
# else:
#     show_grade("F")

#use of or
# def show_grade(grade):
#     print(f"You got: {grade}")
#
# if marks >  80 or marks < 10:
#    print("You are very good or very bad")
#    if marks > 80:
#        print('Excellent')
#    else:
#        print("Not so good")
# else:
#    print("You are ok")

# number = int(input("Give a Number:"))
# the_user_is_good = number >= 80
# message = "The number is greater than or equals 80:" + str(the_user_is_good)
# print(message)

#Loop
# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
#
# even_numbers = []
# starting = 0
# user_input = int(input("Limit: "))
# while starting <= user_input:
#     if is_even(starting):
#       even_numbers.append(starting)
#     starting = starting + 1

# for num in range(0, user_input + 1):
#     if is_even(num):
#         even_numbers.append(num)
#
# print(f"Even Numbers: {even_numbers}")
#
# grocery = ["rice", "water", "tomato", "ginger"]

# for item in grocery:
#     if item == "water":
#     #continue #for not showing water
#        break #will exit from the loop
#     print(item)

# for i in range(0, len(grocery)):
#     print(grocery[i])


# #Read and write from files
# with open("Shakespeare.txt", mode = "r") as s_file:
#     words_all = []
#     for line in s_file.readlines():
#         words = line.strip().split(" ")
#         words_all += words #for adding words_all with words list
#
#         unique_words = set(words_all)
#         print(len(words_all))
#         print(len(unique_words))
    #print(line.strip())

    # with open("unique_words.txt", mode = "w") as write_file:
    #     for item in sorted(unique_words):
    #         write_file.write(item)
    #         write_file.write("\n")

#Debugging
username = input("Your Name: ")
# value = 1
# string_value = str(value)
# new_string = string_value + username
# print(new_string)

for i in range(10):
    print(i)
print("Finished")

#Prime Number
import math
user_number = int(input("Upper Limit for Prime: "))

def is_prime(number):
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
        return True

for i in range(1, user_number + 1):
    if is_prime(i):
        print(i)




