number_of_people = int(input())
capacity = int(input())

full_courses = number_of_people // capacity
partial_courses = number_of_people % capacity
result = 1

if number_of_people <= capacity:
    print(result)
elif not partial_courses == 0:
     print(full_courses + 1)
else:
    print(full_courses)

