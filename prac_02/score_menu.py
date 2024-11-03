print("""(G)et a valid score (must be 0-100 inclusive)
(P)rint result 
(S)how stars
(Q)uit""")
def main():
    score=70
    choice=input("Decide a choice: ").upper()
    while choice!="Q":
        if choice=="G":
            score=get_score()
        elif choice=="P":
            a=print_result(score)
            print(a)
        elif choice=="S":
            show_stars(score)
        else:
            print("Invalid choice")
        print()

        print("""(G)et a valid score (must be 0-100 inclusive)
        (P)rint result 
        (S)how stars
        (Q)uit""")
        choice = input("Decide a choice: ").upper()
    quit()

def get_score():
    score=int(input("Enter your score: "))
    while score<0 or score>100:
        print("Invalid score")
        score=int(input("Enter your score: "))
    return score

def print_result(score):
    if score < 0 :
        return ("Invalid score")
    elif score > 100:
        return("Invalid score")
    elif score >= 50 and score<90:
        return("Passable")
    elif score >= 90:
        return("Excellent")
    else:
        return("Bad")

def show_stars(score):
    print("*"*score,end="")

def quit():
    print("farewell")

main()
