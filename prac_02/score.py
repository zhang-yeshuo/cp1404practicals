def main():
    score = float(input("Enter score: "))
    result=get_scores(score)
    print(result)


def get_scores(score):
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

main()



