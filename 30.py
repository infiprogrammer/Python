# write a function stats

def stats(filename):
    f = open(filename, "r")
    content = f.read()
    print(content)
    f.close()

    lines = content.split("\n")
    print(lines)

    words = content.split()
    print(words)

    print("Number of lines=", len(lines))
    print("Number of words=", len(words))
    print("Number of character=", len(content)-(len(lines)-1))
    print(len(content))
stats("sample_document.txt")