#Author: xiaoyu hao

old_dog_age = 20

count = 0
while count < 3:

    guess_age = int(input("Please input guess age: "))

    if guess_age == old_dog_age:
        print("yes,very good!")
        break
    elif guess_age < old_dog_age:
        print("THink oldder!")
    else:
        print("think smaller!")
    count +=1
else:
    print("You tries many times,ByeBye...")

