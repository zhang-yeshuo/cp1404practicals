from prac_06.programming_language import ProgrammingLanguage
def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)
    print("The dynamically typed languages are:")
    list=[python,ruby,visual_basic]
    for i in list:
        if i.is_dynamic()==True:
            print(i.name)
main()