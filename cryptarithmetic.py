from itertools import permutations


def run():
    word1 = input("Enter first word: ").upper()
    word2 = input("Enter second word: ").upper()
    result = input("Enter result word: ").upper()

    if not word1 or not word2 or not result:
        print("Words cannot be empty.")
        return

    letters = set(word1 + word2 + result)
    first_letters = {word1[0], word2[0], result[0]}
    found = False

    if len(letters) > 10:
        print("No solution possible")
        return

    for digits in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, digits))

        if any(mapping[letter] == 0 for letter in first_letters):
            continue

        a = int("".join(str(mapping[x]) for x in word1))
        b = int("".join(str(mapping[x]) for x in word2))
        c = int("".join(str(mapping[x]) for x in result))

        if a + b == c:
            print("\nSolution Found")
            print(mapping)
            print(a, "+", b, "=", c)
            found = True
            break

    if not found:
        print("No solution found")


if __name__ == "__main__":
    run()
