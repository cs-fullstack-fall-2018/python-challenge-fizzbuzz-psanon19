import os
os.system("clear")

my_file = open ("fizz.txt","w+")
my_file2 = open("buzz.txt", "w+")
my_file3 = open("fizzBuzz.txt", "w+")

enterNumber = int(input("What is your final number?: "))
for numberCount in range(1, enterNumber):
    if numberCount%3==0 and numberCount%5==0:
        my_file3.write(str(numberCount) + "\n")
        print("FIZZBUZZ", numberCount)
    elif numberCount%3==0:
        my_file.write(str(numberCount) + "\n")
        print("FIZZ", numberCount)
    elif numberCount%5==0:
        my_file2.write(str(numberCount) + "\n")
        print("BUZZ", numberCount)
    else:
        print(numberCount)

