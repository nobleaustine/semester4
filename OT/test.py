# constraints = ["-1x1 + -1x2 < -1","-2x1 + -3x2 < -2"]
# z           = "-3x1 + -1x2"
 

# 1 2 3 4
# 


# 0 2 2 1
# 4 6 8 6
# 6 8 10
from tabulate import tabulate

def merge_cells(table, row, col_start, col_end):
    for i in range(col_start, col_end + 1):
        table[row][i] = None

table = [
    ["Name", "Age", "Country"],
    ["John (merged)", 25, "USA"],
    ["Alice", 32, "Canada"],
    ["Mark", 28, "Australia"]
]

# Merge cells in the second row (John's information)
merge_cells(table, 1, 0, 1)

# Generate the table with merged cells
table_str = tabulate(table, headers="firstrow", tablefmt="grid")
print(table_str)