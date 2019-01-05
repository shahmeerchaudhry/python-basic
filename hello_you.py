#ask user for name
name = input("What is your name?: ")

#ask user for age

age = input("How old are you?: ")


#ask user for city

city = input("Where are you from?: ")


#ask user what they enjoy

love = input("What do you love to do: ")

#create output text

string = "Your name is {} and you are {} years old. You live in {} and you love to {}"
output = string.format(name, age, city, love)


#print output to screen
print(output)
