# Step 1: Initial Facts
facts = {"A", "B"}

# Step 2: Rules
# (Conditions, Conclusion)
rules = [
    (["A", "B"], "C"),
    (["C"], "D"),
    (["D"], "E"),
    (["E"], "F")
]

print("Initial Facts:", facts)

print("\nForward Chaining Process:\n")

new_fact = True

# Repeat until no new fact is generated
while new_fact:
    new_fact = False

    # Check every rule
    for conditions, conclusion in rules:

        # Are all conditions true?
        if all(condition in facts for condition in conditions):

            # Add new fact if not already present
            if conclusion not in facts:
                facts.add(conclusion)

                print(conditions, "->", conclusion)

                new_fact = True

print("\nFinal Facts:")
print(facts)
