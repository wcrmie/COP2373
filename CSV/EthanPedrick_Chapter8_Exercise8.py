# This program allows an instructor to keep a record of any amount of grades, tied to a student in a CSV file. Ethan Pedrick, Exercise 8

import csv

# Define a list to hold a student's traits in order before recording them.
list = []


def main():

    count = 0

    while (count <= 0):
        try:

            count = int(input("How many students would you like to record grades for?"))

        except:

            print("Ensure you input a positive integer.")

    with open("students.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["First Name", "Last Name", "First Exam Grade", "Second Exam Grade", "Third Exam Grade"])

        for x in range (count):

            writer.writerow(getStudentInfo())



def getStudentInfo():

    list = [
        input("Input the student's first name."),
        input("Input the student's last name."),
        input("Input the student's first exam grade."),
        input("Input the student's second exam grade."),
        input("Input the student's third exam grade.")
    ]

    return list

main()