count = 0
min_g = 1
max_g = 100
guess = 50

def main():
    print("Think of an integer between 1 and 100")
    ask(guess)

def ask(guess):
    global count
    if guess < 1:
        print("Don't lie!")
        quit()

    ans = input(f"Is the number {guess}?\n(yes/no): ")
    if ans.lower().startswith("y"):
        count += 1
        print(f"I guessed correctly in {count} attempts.")
    else:
        count += 1
        ask_hint(guess)

def ask_hint(guess):
    global min_g, max_g
    h_ans = input(f"Is the number smaller than {guess}?\n(yes/no): ")
    if h_ans.lower().startswith("y"):
        max_g = guess - 1
        calculate(guess)
    else:
        min_g = guess + 1
        calculate(guess)

def calculate(guess):
    global min_g, max_g
    temp_g = max_g - min_g
    guess = round(max_g - temp_g / 2)
    ask(guess)

if __name__ == '__main__':
    print('Guessing game')
    main()