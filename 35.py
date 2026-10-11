# Implement a function distribution () that takes as input the name of a file (as)

def distribution(filename):
    try:
        with open(filename,'r') as f:
           grades_line = f.read()
           grades = grades_line.split()
           print(grades)
        c = dict()
        for i in grades:
            if i in c:
               c[i] += 1
            else:
                c[i] = 1
                print(c)        
        grade_order = ["A","A-","B","B-","C","C-","D","D+","F"]
        print("Grade Distribution:")
        for grade in grade_order:
               count = c.get(grade,0)
               print(f"students who got grade {grade} = {count}")
    except FileNotFoundError:
        print(f"Error: The file'{filename}' wasn't found.")
    except Exception as e:
        print(f"An error occurred: {e}")
      
# Function call:      
distribution("test_file.txt")  