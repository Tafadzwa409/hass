
while True:
    try:
        age = int(input("Please enter your age: "))
    except ValueError:
        print("Sorry i dont understand.")
        continue
    else:
        break

if age >= 18:
     print("Looks like we are both adults")
else:
    print("You are still a kid haha")

while True:
    name = input("What is your name, and please put it in 'CAPS': ")
    if not name.isupper():
        print("Your name is not in CAPS, please do the right thing")
    else:
        break

print("Hello",name,"i am Tafadzwa.")
hobby = input("What is your favorite hobby: ")
print(hobby,"is my favorite hobby too")

while True:
    try:
        number = int(input("Enter a number and i will tell you if it's odd or even: "))
    except ValueError:
        print("This is not a number and you know it so quite being an idiot.")
        continue
    else:
        break
if number % 2 == 0:
    print("\nThe number " + str (number) + " is even.")
else:
    print("\nThe number " + str (number) + " is odd.")

print("The development is still underway... see you soon Bye.")