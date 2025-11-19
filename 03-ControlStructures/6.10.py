dog_age = 0
age = int(input("Enter age: "))
if age <= 2 and age >= 0:
    dog_age = age * 10.5
else:
    dog_age = 10.5 * 2
    age = age - 2
    dog_age = dog_age + (age * 4)
print(f"The dog's age in dog years is: {dog_age}")

