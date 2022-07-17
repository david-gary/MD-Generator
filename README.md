# Markdown Template Generator

## Description

Script with a command line interface to generate markdown templates I commonly use. Written in Python and intended to be placed in a bashrc/zshrc with an alias to execute. Meant to produce a lightweight, modular file structure and eliminate some of the more tedious syntax typing.

## Template Types

- Project Planner
  - Takes in milestone number input
  - Generates a timeline of task completion and subsections for each milestone
- Weekly Planner
  - Sections with individual task lists for each day
- Notes Template
  - Takes in the course name, labels the header as `Course Name - Date`
  - Writes in a few of subsections with bullet points
- README Template
  - Takes in a project name
  - Sections included: Description, Requirements, Usage, and Future Work
  - Requirements and Usage follow my normal bash script project execution form
