#Lab 09 Kathryn Peters
def encode(password):
    encoded_pw = ""
    for i in password:
        new = int(i)+3
        encoded_pw += str(new)

    return encoded_pw


def main():
    choose = 0
    while choose != 3:
        #Print menu
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choose = int(input("\nPlease enter an option: "))

        if choose == 1:
            password = input("Please enter your password to encode: ")
            encode(password)
            print("Your password has been encoded and stored!\n")

        elif choose == 2:
            pass

if __name__ == "__main__":
    main()