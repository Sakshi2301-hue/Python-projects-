import random
 
secret_number = random.randint(1,100)
attempt = 0

print("Guess the Number between 1 to 100")

while True:
    guess = int(input("Guess a number: "))
    attempt += 1

    if guess < secret_number:
        print("Too LOW")

    elif guess > secret_number:
        print("Too HIGH")

    else:
        print(f"Congratulations! You guessed the number in {attempt} attempts.")
        break
