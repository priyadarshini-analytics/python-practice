import time
import random

sentesnces = [
    "The quick brown fox jumps over the lazy dog.", 
    "Typing is a skill that improves with practice.",
    "Python is a versatile programming language.",
    "Consistency is key to mastering any skill.",
    "Practice makes perfect, so keep typing!" 
]

def major_accuracy(user_input, sentence):
    correct_chars = sum(1 for a, b in zip(user_input, sentence) if a == b)
    total_chars = len(sentence)
    accuracy = (correct_chars / total_chars) * 100
    return accuracy


def typing_speed_tester():
    print("Welcome to the Typing Speed Tester!")
    print("You will be given a sentence to type. Type it as fast and accurately as you can.")
    input("Press Enter to start...")

    sentence = random.choice(sentesnces)
    print("\nType the following sentence:")
    print(sentence)

    start_time = time.time()
    user_input = input("\nYour input: ")
    end_time = time.time()

    elapsed_time = end_time - start_time
    words_typed = len(user_input.split())
    speed = words_typed / (elapsed_time / 60)  # words per minute

    accuracy = sum(1 for a, b in zip(user_input, sentence) if a == b) / len(sentence) * 100

    print(f"\nTime taken: {elapsed_time:.2f} seconds")
    print(f"Typing speed: {speed:.2f} words per minute")
    print(f"Accuracy: {accuracy:.2f}%")

typing_speed_tester()






































