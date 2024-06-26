#Lab 09 Kathryn Peters
def encode(password):
    encoded_pw = ""
    for i in password:
        new = int(i)+3
        encoded_pw += str(new)

    return encoded_pw

# print(encode("12345"))
# Sabrina Is Here!
def decoder(encoded_pw):
    decoded_pw = ''
    for num in encoded_pw:
        decoded_digit = str(int(num) - 3)  # Shifting each digit down by 3
        decoded_pw += decoded_digit
    return decoded_pw
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
            print(f"The encoded password is {encode(password)}, and the original password is {decoder(encode(password))}.\n")

if __name__ == "__main__":
    main()