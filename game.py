import random

def math_quiz():
    score = 0
    for _ in range(5):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        correct_answer = num1 + num2
        
        try:
            user_answer = int(input(f"What is {num1} + {num2}? "))
            if user_answer == correct_answer:
                print("Correct! Well done.")
                score += 1
            else:
                print(f"Wrong! The correct answer was {correct_answer}.")
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    print(f"Your final score is {score}/5.")

def word_scramble():
    words = ["apple", "banana", "grape", "orange", "mango"]
    word = random.choice(words)
    scrambled = ''.join(random.sample(word, len(word)))
    
    print(f"Unscramble this word: {scrambled}")
    user_guess = input("Your answer: ")
    
    if user_guess.lower() == word:
        print("Correct! You got it right.")
    else:
        print(f"Wrong! The correct word was {word}.")

def main():
    print("Welcome to the Kids' Mind Game!")
    while True:
        print("\nChoose a game:")
        print("1. Math Quiz")
        print("2. Word Scramble")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            math_quiz()
        elif choice == "2":
            word_scramble()
        elif choice == "3":
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
