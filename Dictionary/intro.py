# declaration

d1 = {
    "Name" : "Shoyeb",
    "Age" : 19,
    "Profession" : "Student"
}

print(d1)
print(type(d1))

# using dict keyword

d2 = dict(
    name = "Shoyeb",
    Age = 19
)
print(d2)
print(type(d2))
print(d2["name"])

d3 = {
    2 : "Many",
    "Key" : "Values",
    "List" : [1, 45, "Prakhar"],
    "Tuple" : (1, 34, 12, "Shoyeb")
}

print(d3["List"])
print(d3["List"][2])
print(d3["Key"])

#by get method
print(d3.get("Tuple"))


product = {
    "Name" : "Smartwatch",
    "Price" : "₹2399/-",
    "Color": "Solid Black",
    "Warranty" : "2 years",
}

# printing all the values
print(product.values())

# printing all the keys
print(product.keys())

print(product.items())

