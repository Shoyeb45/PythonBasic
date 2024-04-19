def add(a, b):
    '''
        Args:
            Two numbers
        Return:
            This will calculate addition of two numbers
    '''
    return a+b

def table(a):
    '''
        Args:
            Single number
        Return:
            Will print the table of a from 1 to 10.
    '''
    for i in range(1, 10):
        print(f"{a} * {i} = {a*i}")
    
if __name__ == "__main__":
    print("This is custom module")