#!/usr/bin/python3
def main():
    print("Welcome to the email slicer")
    print("")

    email_input = input("Input your enamil address : ")

    result = email_input.split("@")
    print(result.__len__())
    (result[1],extension) = result[1].split(".")

    print("username : ", result[0])
    print("Domain : ", result[1])
    print("extension : ", extension)

main()
'''
TODO: 应该增加输入检错功能
'''
