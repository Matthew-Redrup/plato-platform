import sys
from datetime import datetime


class MenuCLI:
    def __init__(self):
        self.choice = ""
        self.user_input = ""

    def display_menu(self):
        print("\nMenu:")
        print("1. Describe what you would like to learn")
        print("2. Display Current Date")
        print("3. Exit")

    def parse_input(self):
        self.choice = input("\nPlease choose an option (1-3): ")

    def action(self):
        if self.choice == "1":
            self.user_input = input("\nPlease describe what you would like to learn: ")
            print(f"You entered: {self.user_input}")
            return self.user_input
        elif self.choice == "2":
            print(f"\nToday's date is {datetime.now().date()}")
        elif self.choice == "3":
            print("\nExiting the program. Goodbye.")
            sys.exit()
        else:
            print("\nInvalid option. Please try again.")
