from main import run_study_plan, run_quiz, view_resources, view_progress

def menu():
    while True:
        print("\n=== STUDY GUARDIAN ===")
        print("1. Generate Study Plan")
        print("2. Take Quiz")
        print("3. Show Resources")
        print("4. Show Progress")
        print("5. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            run_study_plan()
        elif choice == "2":
            run_quiz()
        elif choice == "3":
            view_resources()
        elif choice == "4":
            view_progress()
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Stupid choice, try again.")

if __name__ == "__main__":
    menu()
