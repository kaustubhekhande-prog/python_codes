def main():
    while True:
        print("\n========== AI PROGRAMS MENU ==========")
        print("1. A* Search Algorithm")
        print("2. N-Queens Problem")
        print("3. Cryptarithmetic Problem")
        print("4. Forward Chaining (code missing in supplied PDF)")
        print("5. Backward Chaining")
        print("6. Chatbot")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            from astar_search import run
        elif choice == "2":
            from n_queens import run
        elif choice == "3":
            from cryptarithmetic import run
        elif choice == "4":
            from forward_chaining import run
        elif choice == "5":
            from backward_chaining import run
        elif choice == "6":
            from chatbot import run
        elif choice == "0":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            continue

        print()
        run()


if __name__ == "__main__":
    main()
