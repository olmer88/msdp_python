from random import randint


n = randint(1, 100)
n_from_user = 0
while n != n_from_user:
    n_from_user = input("I made up a number. Can you guess it?")
    try:
        n_from_user = int(n_from_user)
    except ValueError:
        print("Enter a number")
        continue
    if n_from_user > n:
        print("Too high")
    if n_from_user < n:
        print("Too low")
print('Congratulations you won!')
