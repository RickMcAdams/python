import random
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print ("Rolling the dices...");
    print ("The values are....");
    a = (random.randint(min, max));
    b = (random.randint(min, max));
    print (a," + ", b, " = ", a + b)

    roll_again = input("Roll the dices again?")
