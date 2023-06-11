#!/usr/bin/env python3
import random
import prompt


def main():
    print("Welcome to the Brain Games!")

    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")

    print("Find the greatest common divisor of given numbers.")
    correct_answers_counter = 0

    while correct_answers_counter != 3:
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        print(f"Question: {x} {y}")

        answer = prompt.string("Your answer: ")

        while y:
            x, y = y, x % y

        correct_answer = str(x)

        if answer == correct_answer:
            print("Correct!")
            correct_answers_counter += 1
        else:
            print(
                f"{answer} is wrong answer ;(. "
                + f"Correct answer was {correct_answer}.\n"
                + f"Let's try again, {name}!"
            )
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
