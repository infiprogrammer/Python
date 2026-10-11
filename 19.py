#The cryptography ______________________ the string xxxxxx.

def crypto(filename):
    try: 
        with open(filename,'r')as f:
            content=f.read()
            modified_content=content.replace('write','xxxxxx')
            print(modified_content)
            print("\n")
            print(content)
    except FileNotFoundError:
        print(f"Error:file'{filename}'not found")
    except Exception as e:
        print (f"An error occured:{e}")

crypto("abc.txt")