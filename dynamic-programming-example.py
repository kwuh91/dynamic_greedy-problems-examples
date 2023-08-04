import numpy as np


# dynamic programming

def matr_print(matr):
    print("------")
    for i in matr:
        print(i)


items = {}

items["guitar"] = np.array([1500, 1])
items["recorder"] = np.array([3000, 4])
items["laptop"] = np.array([2000, 3])
items["iphone"] = np.array([2000, 1])

print(f"items({len(items)}) = {items}")


def best_steal(capacity, items):
    cell = [[np.NINF for i in range(capacity)] for j in range(len(items))]
    i: int = -1
    for item in items:
        # print(f"curr item = {item}")  # guitar
        i += 1  # i = 0
        for j in range(capacity):  # 0-3
            curr_weight_category = j + 1  # 1-4
            if i:  # (i != 0)
                if items[item][1] <= curr_weight_category:
                    if curr_weight_category - items[item][1] - 1 >= 0:
                        cell[i][j] = max(cell[i - 1][j], items[item][0] + cell[i - 1][j - items[item][1]])
                    else:
                        cell[i][j] = max(cell[i - 1][j], items[item][0])
                else:
                    cell[i][j] = cell[i - 1][j]
            else:
                if items[item][1] <= curr_weight_category:
                    cell[i][j] = items[item][0]

        matr_print(cell)

    return cell[len(items) - 1][capacity - 1]


ans = best_steal(4, items)
print(f"ans = {ans}")
