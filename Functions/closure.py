def outer():
    a = 10
    def inner():
        print(a)
        return inner

    x = inner()

print()