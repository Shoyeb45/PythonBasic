info = {
    "Name" : "Mitesh",
    "DOB"  : "28 May, 2004",
    "Profession" : "Student",
    "Age" : "20",
    "Dropper" : False
}


# 1. del
del info["Age"]
print(info)

# 2. update()
info.update({"Dropper":True})
info.update({"Age":"19"})
print(info)

# 3.clear
info.clear()
print(info)

# 4.pop

book = {
    "Title" : "Harry Potter and order of the phoenix",
    "Author" : "J K Rowling",
    "Genre" : "Fantasy",
    "Price" : "₹449.00/-",
    "Pages" : "766 pages"
}

book.pop("Pages")
print(book)

# 5. popitem
book.popitem()
print(book)