# creating
t1 = (1, 2, 4, -98, 12, "Shoyeb")
print(type(t1))

t2 = tuple([2, 3, 5])
t3 = tuple()
print(type(t2))
name = tuple("Shoyeb")
print(name)
print(len(name))

t4 = (12)
print(type(t4))
t4 = tuple((12,))
t4 = (12,)
print(type(t4))


# slicing 
print(t1[: :-1])
print(t1[0: -1: 2])