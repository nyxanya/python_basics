

class Customer:
    def __init__(self, fn, ln):
        self.first_name = fn
        self.last_name = ln

def main():
    c = Customer(fn = "Chandra", ln = "Mohan")
    print(c.last_name,",",c.first_name)

if __name__== "__main__":
     main()