name = input("Enter your name:")
choice = input("""(H)ello
(G)oodbye
(Q)uit
""").upper()
while choice != 'Q':
    if choice == 'H':
        print("Hello", name)
    elif choice == 'G':
        print("Goodbye", name)
    else:
        print("Invalid Choice")
    choice = input("""(H)ello
(G)oodbye
(Q)uit
""").upper()
print('Finished')
