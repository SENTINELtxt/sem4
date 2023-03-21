# Implement a greedy algorithm and find the optimal solution to the fractional Knapsack
# instance n = 7, m = 15, (p1 p2 p3 p4 ......p7) = (1, 5, 10, 10, 5, 7, 8) and
# (w1, w2..........w7) = (3, 2, 5, 7, 2, 8, 4).

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight


def fractional_knapsack(capacity, items):
    items.sort(key=lambda x: x.ratio, reverse=True)
    max_value = 0
    for item in items:
        if capacity == 0:
            return max_value
        elif item.weight <= capacity:
            capacity -= item.weight
            max_value += item.value
        else:
            max_value += capacity * item.ratio
            capacity = 0
    return max_value


if __name__ == "__main__":
    W = 15
    values = [1, 5, 10, 10, 5, 7, 8]
    weights = [3, 2, 5, 7, 2, 8, 4]
    items = [Item(values[i], weights[i]) for i in range(len(values))]
    n = len(weights)
    print("Fractional Knapsack in Python")
    print("Knapsack Capacity:", W)
    print("Item\tWeight\tValue")
    for i in range(n):
        print(f"{i+1}\t{weights[i]}\t{values[i]}")
    max_value = fractional_knapsack(W, items)
    print("Maximum profit:", max_value)


# OUTPUT
# Fractional Knapsack in Python
# Knapsack Capacity: 15
# Item    Weight  Value
# 1       3       1
# 2       2       5
# 3       5       10
# 4       7       10
# 5       2       5
# 6       8       7
# 7       4       8
# Maximum profit: 30.857142857142858
