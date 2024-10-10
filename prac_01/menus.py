MENU = """(H)ello
(G)oodbye
(Q)uit"""
name=input("Enter name: ")
choice=0
while choice!="Q":
    print(MENU)
    choice = input(">>> ").upper()
    if choice=="H":
        print(f"Hello {name}")
    elif choice=="G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
print("Finished.")

