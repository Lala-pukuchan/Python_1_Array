from array2D import slice_me

print("--------------------")
print("normal case: ")
family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
print(slice_me(family, 0, 2))
print("--------------------")
print("normal case: ")
print(slice_me(family, 1, -2))

print("--------------------")
print("list length error handling: ")
family = [[78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
print(slice_me(family, 0, 2))

print("--------------------")
print("list error handling: ")
family = 0
print(slice_me(family, 0, 2))
