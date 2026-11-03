def minimax(a, mx=True):
    if len(a) == 1:
        return a[0]

    m = len(a) // 2
    x = minimax(a[:m], not mx)
    y = minimax(a[m:], not mx)

    return max(x, y) if mx else min(x, y)


n = int(input("Enter leaf nodes: "))
a = list(map(int, input("Enter values: ").split()))

if n <= 0 or len(a) != n:
    raise ValueError("Enter a positive leaf count matching the number of values.")

print("Optimal value =", minimax(a))
