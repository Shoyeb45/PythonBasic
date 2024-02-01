city = {"Ahemdabad", "Bhuj", "Kolkata", "Bangalore", "Bhuj"}
state = {"Gujarat", "West Bengal", "Karnataka", "Jharkhand", "West Bengal"}

# 1. union and update
city.update(state)
print(city)
print(state.union(city))

# 2. intersection and intersection_update()
A = {1, 3, 3, 4, 6, 7, 1, 8, 90, -12}
B = {3, 5, 6, 1, -12, 13, 15}
B.intersection_update(A)
print(B)  
print(A.intersection(B))

# 4.  symmetric_difference and symmetric_difference_update()
C = {12, 50, 12, 34, 56}
D = {12, 58, 12, 23, 90, 56, 50}
C.symmetric_difference_update(D)
print(C)
print(D.symmetric_difference(C))

# 5. difference() and difference_update()

E = {12, 50, 800, 34, -98, 56}
F = {122, 58, 12, 800, 90, 56, 50}
print("")
print(C.difference(D))
D.difference_update(C)
print(D)
