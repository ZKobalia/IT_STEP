import random
import datetime

class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        while True:
            publication_year = input("Enter publication year: ")
            current_year = datetime.datetime.now().year

            if publication_year.isdigit() and 0 < int(publication_year) <= current_year:
                break
            else:
                print("Invalid year. Please enter a valid publication year.")

        new_book = Book(title, author, int(publication_year))
        self.books.append(new_book)
        print(f"Book '{title}' added successfully.")

    def view_all_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("List of Books:")
            for book in self.books:
                print(f"Title: {book.title}, Author: {book.author}, Publication Year: {book.publication_year}")

    def search_book(self, title):
        found_books = [book for book in self.books if book.title.lower() == title.lower()]
        if found_books:
            print("Found Books:")
            for book in found_books:
                print(f"Title: {book.title}, Author: {book.author}, Publication Year: {book.publication_year}")
        else:
            print(f"No books found with the title '{title}'.")

def run_calculator():
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero"

    def get_number_input(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def get_operation_choice():
        while True:
            choice = input("Choose Operation (+, -, *, /): ")
            if choice in ('+', '-', '*', '/'):
                return choice
            else:
                print("Invalid operation. Please choose a valid operation.")

    while True:
        print("Calculator")

        num1 = get_number_input("Enter first number: ")
        num2 = get_number_input("Enter second number: ")

        choice = get_operation_choice()

        if choice == '+':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '-':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '*':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '/':
            print(num1, "/", num2, "=", divide(num1, num2))

        another_calculation = input("If you want to perform another calculation print 'yes': ")
        if another_calculation.lower() != 'yes':
            print("Exiting the calculator. Goodbye!")
            break

def run_guess_number_game():
    def guess_number_game():
        while True:
            max_attempts = 7
            print("Welcome to the Number Guessing Game!")
            print(f"I have selected a number between 1 and 100. Can you guess it in {max_attempts} attempts? \n")

            secret_number = random.randint(1, 100)

            attempts = 0
            guessed_correctly = False

            while attempts < max_attempts:
                try:
                    guess = int(input(f"Attempt {attempts+1}. Enter your guess: "))
                    if guess < 1 or guess > 100:
                        print("Invalid input! Please enter a number between 1 and 100.")
                        continue
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
                    continue

                attempts += 1

                if guess == secret_number:
                    print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
                    guessed_correctly = True
                    break
                elif guess < secret_number:
                    print("Too low! Try again. \n")
                else:
                    print("Too high! Try again. \n")

            if not guessed_correctly:
                print(f"Sorry, you've reached the maximum number of attempts. The correct number was {secret_number}.")

            play_again = input("If you want to play again, type 'yes': ").lower()
            if play_again != 'yes':
                print("Thanks for playing. Goodbye!")
                break

    guess_number_game()

def run_hangman():
    def choose_word():
        words = ["python", "hangman", "programming", "developer", "coding", "computer", "encyclopedia"]
        return random.choice(words)

    def display_word(word, guessed_letters):
        return ''.join(letter if letter in guessed_letters else '_' for letter in word)

    def hangman():
        print("Welcome to Hangman!")
        
        while True:
            word_to_guess = choose_word().lower()
            guessed_letters = set()
            attempts_left = int(len(word_to_guess) * 1.5)

            while True:
                current_display = display_word(word_to_guess, guessed_letters)
                print(f"\nWord: {current_display}")
                print(f"Attempts left: {attempts_left}")
                
                if current_display == word_to_guess:
                    print("Congratulations! You've guessed the word.")
                    break
                
                if attempts_left == 0:
                    print(f"Sorry, you've run out of attempts. The correct word was '{word_to_guess}'.")
                    break

                guess = input("Enter a letter or the whole word: ").lower()

                if guess.isalpha() and len(guess) == 1:
                    if guess in guessed_letters:
                        print("You've already guessed that letter. Try again.")
                        continue

                    guessed_letters.add(guess)

                    if guess not in word_to_guess:
                        print("Incorrect guess!\n")
                        attempts_left -= 1
                elif guess.isalpha() and len(guess) > 1:
                    if guess == word_to_guess:
                        print("Congratulations! You've guessed the word.")
                        break
                    else:
                        print("Incorrect guess!\n")
                        attempts_left -= 1
                else:
                    print("Invalid input! Please enter a single letter or the whole word.")
                    continue

            play_again = input("If you want to play again, type 'yes': ").lower()
            if play_again != 'yes':
                print("Thanks for playing Hangman. Goodbye!")
                break

    hangman()

if __name__ == "__main__":
    book_manager = BookManager()

    while True:
        print("\nOptions:")
        print("1. Calculator")
        print("2. Guess Number Game")
        print("3. Hangman Game")
        print("4. Book Manager")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            run_calculator()
        elif choice == "2":
            run_guess_number_game()
        elif choice == "3":
            run_hangman()
        elif choice == "4":
            while True:
                print("\nBook Manager Options:")
                print("1. Add a new book")
                print("2. View all books")
                print("3. Search for a book")
                print("4. Exit")

                book_choice = input("Enter your choice (1-4): ")

                if book_choice == "1":
                    title = input("Enter book title: ")
                    author = input("Enter author: ")
                    book_manager.add_book(title, author)
                elif book_choice == "2":
                    book_manager.view_all_books()
                elif book_choice == "3":
                    search_title = input("Enter the title of the book to search: ")
                    book_manager.search_book(search_title)
                elif book_choice == "4":
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
