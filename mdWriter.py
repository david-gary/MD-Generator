import os
import sys
import datetime


def make_new_md_file():
    # get user input for what the file should be called
    user_input = input("Start with the name of your file.\nDo not include the '.md' extension.\nFile names will look cleaner and be easier to find/write to without any spaces between words.\nEnter your file name here: ")
    # use os to see current directory contents
    file_name = user_input + ".md"
    cwd = os.getcwd()
    # check if file already exists
    if os.path.exists(file_name):
        while True:
            print(
                f"File {file_name} already exists in the current directory ({os.getcwd()}).")
            overwrite = input("Would you like to overwrite the file? (y/n): ")
            if overwrite == "y":
                break
            elif overwrite == "n":
                user_input = input("Enter a new file name here: ")
                file_name = user_input + ".md"
                if not os.path.exists(file_name):
                    break
            else:
                print("Invalid input. Requesting new file name.")
                user_input = input("Enter a new file name here: ")
                file_name = user_input + ".md"
                if not os.path.exists(file_name):
                    break
    return file_name


def add_header(file_name):
    header_input = input("Enter your file's header here: ")
    with open(file_name, "w") as f:
        # add the header to the file, then add a blank line, then save the file.
        header_line = "# " + header_input + "\n\n"
        f.write(header_line)


def project_planning_template(file_name):
    # begin new file content additions
    # add overview section
    new_file_content = "## Overview\n\n"
    # get number of milestones
    num_milestones = int(
        input("Enter the number of project milestones here: "))

    new_file_content = "## Timeline\n\n"
    new_file_content += "| |Milestone|Deadline|Status|\n"
    new_file_content += "|-|---------|--------|------|\n"
    current_date = datetime.datetime.now()
    # crop the date to the month and day
    for i in range(num_milestones):
        month_day = current_date.strftime("%m/%d")
        new_file_content += f"|{i+1}|Name|{month_day}|✅ or ❌|\n"
        # update the date by one week
        current_date += datetime.timedelta(days=7)

    new_file_content += "\n"

    for i in range(num_milestones):
        new_file_content += f"## {i+1}) Milestone\n\n"
        new_file_content += f"- Task 1\n- Task 2\n- Task 3\n\n"

    # trim the file content to remove the last newline
    new_file_content = new_file_content[:-1]

    with open(file_name, "a") as f:
        f.write(new_file_content)


def week_planner(file_name):

    # get week values
    current_date = datetime.datetime.now()
    end_of_week = current_date + datetime.timedelta(days=7)
    current_weekday = current_date.strftime("%A")

    # crop the date to the month and day
    month_day = current_date.strftime("%m/%d")
    end_of_week = end_of_week.strftime("%m/%d")

    new_file_content = f"# Weekly Planner {month_day} - {end_of_week}\n"

    for i in range(7):
        new_file_content += "\n"
        new_file_content += f"## {current_weekday}\n\n"
        new_file_content += f"- [ ] Task 1\n- [ ] Task 2\n- [ ] Task 3\n"
        current_date += datetime.timedelta(days=1)
        current_weekday = current_date.strftime("%A")

    with open(file_name, "w") as f:
        f.write(new_file_content)


def notes_template(file_name):
    # get week values
    current_date = datetime.datetime.now()
    month_day = current_date.strftime("%m/%d")

    course_name = input("Enter the name of the course here: ")
    new_file_content = f"# {course_name} Notes - {month_day}\n"

    for i in range(3):
        new_file_content += "\n"
        new_file_content += f"## Subtopic {i+1}\n\n"
        new_file_content += f"- Note1\n- Note2\n- Note3\n"
    with open(file_name, "w") as f:
        f.write(new_file_content)


def readme_template(file_name):
    # get the project name
    project_name = input("Enter the name of the project here: ")

    new_file_content = f"# {project_name}\n\n"
    new_file_content += "## Description\n\n"
    new_file_content += "Enter the project description here.\n\n"
    new_file_content += "## Requirements\n\n"
    for i in range(3):
        new_file_content += f"- Requirement {i+1}\n\n"
    new_file_content += "## Usage\n\n"
    phase, cmd = "Installation", "chmod +x setup.sh\nchmod +x run.sh\npip install -r requirements.txt\n./setup.sh"
    for i in range(2):
        new_file_content += f"- {phase}\n"
        new_file_content += "\n```bash\n" + cmd + "\n```\n\n"
        cmd = "./run.sh"
        phase = "Execution"
    new_file_content += "## Future Work\n\n"
    new_file_content += "Enter future work here.\n"
    with open(file_name, "w") as f:
        f.write(new_file_content)


def determine_project_type(file_name):
    print("Template Types\na) Project Planning\nb) Week Planner\nc) Notes Template\nd) Readme Template")
    user_input = input(
        "Enter the template type you want to use here: ").lower().strip()
    if user_input == "a":
        add_header(file_name)
        project_planning_template(file_name)
    elif user_input == "b":
        week_planner(file_name)
    elif user_input == "c":
        notes_template(file_name)
    elif user_input == "d":
        readme_template(file_name)
    else:
        print("Invalid input.\nEnter a for Project Planning or b for Weekly Planner here: ")
        determine_project_type(file_name)


def main():
    file_name = make_new_md_file()
    determine_project_type(file_name)


if __name__ == "__main__":
    main()
