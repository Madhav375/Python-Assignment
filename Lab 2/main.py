'''
 Name: Madhav Kalra
Date: 22/11/2025
Gradebook Analyser Assignment
'''

import csv
print('Welcome! This is a program that analyses student grades.')

def AVG(marks_dict):
    '''calculate average of the marks, which are values in the dictionary
       passed as argument where student names are keys
       returns float type average marks'''
    
    if not marks_dict:
        return 0
    total = sum(marks_dict.values())
    return total / len(marks_dict)

def MEDIAN(marks_dict):
    '''calculates the median of marks, which are values in the dictionary
       passed as argument where student names are keys
       returns float type median score'''
    
    if not marks_dict:
        return 0
    
    # get marks inside a list
    scores = list(marks_dict.values())
    # sort the list
    scores.sort()
    
    n = len(scores)
    mid = n // 2
    
    # if odd length, take the middle element
    if n % 2 != 0:
        return scores[mid]
    # if even length, average the two middle elements
    else:
        return (scores[mid - 1] + scores[mid]) / 2

def MAX(marks_dict):
    '''calculates max marks from the dictionary, 
       returns max. marks of int data type'''

    if not marks_dict:
        return 0
    return max(marks_dict.values())

def MIN(marks_dict):
    '''calculates the min marks from the dictionary,
       returns min. marks of int data type'''

    if not marks_dict:
        return 0
    return min(marks_dict.values())

def main():

    while True:
        print("\n=== Gradebook Menu ===")
        print("1. Manual Input")
        print("2. CSV Input")
        print("3. Exit Program")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Error: Please enter a number.")
            continue # skips to the next iteration of the loop

        if choice == 3:
            print("Exiting Gradebook Analyzer. Goodbye!")
            break # break out of innermost while loop
        
        if choice not in (1, 2):
            print("Error: Invalid Input. Please select 1, 2, or 3.")
            continue

        marks_dict = {}

        if choice == 1:
            try:
                n = int(input("Enter the number of students: "))
                for i in range(n):
                    name = input(f"Enter name for student {i+1}: ")
                    marks = int(input(f"Enter marks for {name}: "))
                    marks_dict[name] = marks
            except ValueError:
                print("Error: Marks must be integers.")
                continue # restart loop if any error
        
        elif choice == 2:
            try:
                with open("marks.csv", "r") as file:
                    reader = csv.reader(file)
                    for data_row in reader:
                        if data_row: 
                            name = data_row[0]
                            marks = int(data_row[1]) 
                            marks_dict[name] = marks
            except FileNotFoundError:
                print("Error: 'marks.csv' file not found.")
                continue
            except ValueError:
                 print("Error: CSV contains invalid data.")
                 continue
        
        print("\n--- Analysis_Result ---")
        print(f"Average:\t{AVG(marks_dict)}") 
        print(f"Median:\t\t{MEDIAN(marks_dict)}")
        print(f"Max Score:\t{MAX(marks_dict)}")
        print(f"Min Score:\t{MIN(marks_dict)}")

        grades = {}
        a, b, c, d, f = 0, 0, 0, 0, 0
        
        for name in marks_dict:
            grade = ""
            marks = marks_dict[name]
            if marks >= 90:
                grade = "A"
                a += 1
            elif marks >= 80:
                grade = "B"
                b += 1
            elif marks >= 70:
                grade = "C"
                c += 1
            elif marks >= 60:
                grade = "D"
                d += 1
            else:
                grade = "F"
                f += 1
            grades[name] = grade
        
        print("\nGrades\t\tTotal Students")
        print(f"A\t\t{a}\nB\t\t{b}\nC\t\t{c}\nD\t\t{d}\nF\t\t{f}")

        passed_students = [x for x in marks_dict if marks_dict[x] >= 40]
        failed_students = [x for x in marks_dict if marks_dict[x] < 40]
        
        print("-" * 40)
        print(f"Total Passed Students: {len(passed_students)}")
        print(f"Names: {', '.join(passed_students)}")
        print(f"Total Failed Students: {len(failed_students)}")
        print(f"Names: {', '.join(failed_students)}")

        print("\nName\t\tMarks\t\tGrade")
        print("-" * 35)
        for name, marks in marks_dict.items():
            print(f"{name}\t\t{marks}\t\t{grades[name]}")
        
        print("\n" + "-"*40 +"\n")

main()
