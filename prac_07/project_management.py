import datetime
from project import Project

def main():
    projects = load_projects("projects.txt")
    while True:
        print("Menu:")
        print("L - Load projects")
        print("S - Save projects")
        print("D - Display projects")
        print("F - Filter projects by date")
        print("A - Add new project")
        print("U - Update project")
        print("Q - Quit")

        choice = input(">>> ").upper()
        if choice == 'L':
            filename = input("Filename to load: ")
            projects = load_projects(filename)
        elif choice == 'S':
            filename = input("Filename to save: ")
            save_projects(filename, projects)
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            date_str = input("The date you want to filter: ")
            print(f"Show projects that start after date (dd/mm/yy): {date_str}")
            filter_projects_by_date(projects, date_str)
        elif choice == 'A':
            print("Let's add a new project")
            add_new_project(projects)
        elif choice == 'U':
            update_project(projects)
        elif choice == 'Q':
            save_choice = input("Would you like to save to projects.txt? ").lower()
            if save_choice == 'y':
                save_projects("projects.txt", projects)
            break
        else:
            print("Invalid choice. Please try again.")

def load_projects(filename):
    projects = []
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines[1:]:
            data = line.strip().split('\t')
            name = data[0]
            start_date = datetime.datetime.strptime(data[1], "%d/%m/%Y").date()
            priority = int(data[2])
            cost_estimate = float(data[3])
            completion_percentage = int(data[4])
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    print(f"You have successfully loaded {filename}")
    return projects

def save_projects(file_name, projects):
    with open(file_name, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate:.2f}\t{project.completion_percentage}\n")
    print(f"You have successfully saved {file_name}")


def display_projects(projects):
    complete = [project for project in projects if project.completion_percentage == 100]
    incomplete = [project for project in projects if project.completion_percentage < 100]
    print("Incomplete Projects:")
    for project in sorted(incomplete, key=lambda x: x.priority):
        print(project)
    print("Completed Projects:")
    for project in sorted(complete, key=lambda x: x.priority):
        print(project)


def filter_projects_by_date(projects, date_str):
    filter_date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.start_date > filter_date]
    for project in sorted(filtered_projects, key=lambda x: x.start_date):
        print(project)

def add_new_project(projects):
    name = input("Name: ")
    date_str = input("Start date (dd/mm/yy): ")
    start_date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    completion_percentage = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))

def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i}  {project}")
    choice = int(input("Project choice: "))
    project = projects[choice]
    new_completion = int(input("New Percentage: "))
    project.update_completion(new_completion)
    new_priority = int(input("New Priority: "))
    project.update_priority(new_priority)

if __name__ == "__main__":
    main()

