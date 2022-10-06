import random

def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print("{0} is not a valid number".format(temp))
highest = 1000
answer = random.randint(1,highest)
print(answer)
guess = 0
print("please guess a number 1 and {}".format(highest))

while guess!= answer:
    guess = get_integer((": "))
    if guess == 0:
        break
