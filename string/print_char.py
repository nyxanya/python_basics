

def print_characters(s):
    i = 1
    while i <= len(s):
        print(s[len(s) - i], end=",")
        i += 1
    print()

def main():
    print_characters(s = "YAYAYAYA")

if __name__ == "__main__":
    main()