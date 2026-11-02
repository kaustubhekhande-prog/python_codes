import heapq

GOAL = ((1, 2, 3), (4, 5, 6), (7, 8, 0))


def heuristic(state):
    """Count tiles that are not in their goal position (blank excluded)."""
    return sum(
        state[i][j] != 0 and state[i][j] != GOAL[i][j]
        for i in range(3)
        for j in range(3)
    )


def astar(start):
    queue = [(heuristic(start), 0, start, [start])]
    visited = set()

    while queue:
        f, g, state, path = heapq.heappop(queue)

        if state == GOAL:
            return path

        if state in visited:
            continue
        visited.add(state)

        x, y = next(
            (i, j)
            for i in range(3)
            for j in range(3)
            if state[i][j] == 0
        )

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = [list(row) for row in state]
                new_state[x][y], new_state[nx][ny] = (
                    new_state[nx][ny],
                    new_state[x][y],
                )
                neighbor = tuple(map(tuple, new_state))

                if neighbor not in visited:
                    new_g = g + 1
                    heapq.heappush(
                        queue,
                        (new_g + heuristic(neighbor), new_g,
                         neighbor, path + [neighbor]),
                    )

    return None


def run():
    print("Enter initial state (0 for blank), one row at a time:")
    start = tuple(tuple(map(int, input().split())) for _ in range(3))
    path = astar(start)

    if path:
        print("\nSolution:\n")
        for step, state in enumerate(path):
            print("Step", step)
            for row in state:
                print(*row)
            print("g =", step, "h =", heuristic(state),
                  "f =", step + heuristic(state), "\n")
    else:
        print("No solution found.")


if __name__ == "__main__":
    run()
