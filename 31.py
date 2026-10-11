# """ Calculates and print the disribution of letter grades from a file.
# The input file is expected to be a single line containing letter grades seprated by blank ?

from collections import Counter

def distr(filename):
    try:
        with open(filename,'r') as f:
           grades_line = f.read()
           grades = grades_line.split(',')
           print(grades)
        
           grade_counts = Counter(grades)
           print(grade_counts)
        
           grade_order = ["A","A-","B","B-","C","C-","D","D+","F"]
           print("Grade Distribution:")
           for grade in grade_order:
               count = grade_counts.get(grade,0)
               print(f"students who got grade '{grade}': {count}")
            
    except FileNotFoundError:
        print(f"Error: The file'{filename}' wasn't found.")
    except Exception as e:
        print(f"An error occurred: {e}")
      
# Function call:      
distr("test_file.txt")