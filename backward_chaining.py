facts = {"A", "B"}

rules = [
    (["A", "B"], "C"),
    (["C"], "D"),
    (["D"], "E"),
    (["E"], "F"),
]


def backward(goal):
    print("Trying to prove:", goal)

    if goal in facts:
        print(goal, "is a known fact.")
        return True

    for conditions, result in rules:
        if result == goal and all(backward(item) for item in conditions):
            print("Goal", goal, "proved.")
            return True

    return False


def run():
    goal = input("Enter Goal to Prove: ").upper()
    print("Backward Chaining Process:")

    if backward(goal):
        print("Result: Goal", goal, "is TRUE.")
    else:
        print("Result: Goal", goal, "is FALSE.")


if __name__ == "__main__":
    run()
