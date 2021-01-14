lanka = input("Please enter a string: ")

if lanka == "":
    print("String too short...")
else:
    lanka_length = len(lanka)
    lanka_length_ws = lanka.replace(" ","")
    lanka_length_ws = len(lanka_length_ws)

    print("Length: {0}".format(lanka_length))
    print("Length without spaces: {0}".format(lanka_length_ws))
    print("First character: {0}".format(lanka[0]))
    print("Last character: {0}".format(lanka[-1:]))

    if lanka == lanka[::-1]:
        print("\"{0}\" is a palindrome".format(lanka))
    else:
        print("\"{0}\" is not a palindrome".format(lanka))