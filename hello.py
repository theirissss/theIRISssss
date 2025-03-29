table = [
    [2, 5, 3, 6],
    [4, 1, 5, 3],
    [5, 3, 6, 2]
]

new_table = [[0 for _ in range(4)] for _ in range(3)]

for i in range(3):
    for j in range(4):
        original = table[i][j]
        upper = new_table[i-1][j] if i > 0 else float('-inf')
        left = new_table[i][j-1] if j > 0 else float('-inf')
        max_value = max(upper, left)
        if max_value == float('-inf'):
            new_value = original
        else:
            new_value = max_value + original
        new_table[i][j] = new_value

print("| 项目 | a         | b         | c         | d         |")
print("|------|-----------|-----------|-----------|-----------|")
rows = ["甲", "乙", "丙"]
for i in range(3):
    row = f"| {rows[i]}   "
    for j in range(4):
        row += f"| {new_table[i][j]} "
    row += "|"
    print(row)