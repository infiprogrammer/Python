#"""The function censor() takes the name of a file (a string) as input.The function should open a file
#read it content and then write it into a file 'censored.txt' with this modification.
#every ocurrence of a four letter word is replaced with 'xxxx'."""
def censor(filename):
    try:
        with open(filename,'r') as infile:
            content = infile.read()
            words = content.split()
            print(words)
            censored_words = []
        
            for word in words:
                if len(word.strip(".,;!?")) == 4:
                   censored_words.append('xxxx')
                else:
                   censored_words.append(word)
            print(censored_words)
            censored_content = ' '.join(censored_words)
            print(censored_content)
            
        with open('censored.txt','w') as outfile:
                outfile.write(censored_content)
                
    except FileNotFoundError:
        print(f"Error:the file'{filename}'was not found.")
    except Exception as e:
        print(f"An unexpect error occurred:{e}")
censor("sample_document.txt")
        