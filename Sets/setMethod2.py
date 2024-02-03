A = {2, 3, 5, 7, 11, 13, 17, 23, 29, 31, 37, 41, 2, 3}
B = {6, 8, 9, 10, 12, 14, 15, 16, 18}

# 1.isdisjoint
if A.isdisjoint(B):
    print("The sets are disjoint.")
else:
    print("Sets are not disjoint.")

# 2.issuperset
city1 = {"Ahemdabad", "Bangalore", "Delhi"}
city2 = {"Delhi", "Kolkata", "Ranchi"}
print(city1.issuperset(city2))
city2 = {"Ahemdabad", "Bangalore"}
print(city1.issuperset(city2))

# 3.issubset
print(A.issubset(B)) # since B is not subset of A

# 4.add
city1.add("Jaipur")
print(city1)

# 6.update
A = {12, 34, 54, 80, 11}
B = {10, 34, 11}
A.update(B)
print(A)

# 7.remove
A.remove(11)
print(A)

# 8.Discard
B.discard(32)  #if we've used remove then it have given error
print(B)

# 9.pop
rmv = city1.pop()
print(city1,"\n","Item removed:",rmv)  #everytime different item will be removed

# 10. del keyword
del city1 # now city1 is deleted and we can't access it anymore

# 11.clear
C = {-12.34, 3.14, 98.432, 2.7779, 980.987324}
C.clear()
print(C) # it will print empty set

# 12. checking if item exist in set or not

names = {"Aryan", "Shoyeb", "Prakhar", "Durgesh"}

if "Shoyeb" in names:
    print("Shoyeb is present")
else:
    print("Shoyeb is not present")

