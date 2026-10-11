s='''It was the best of times,it was the worst of times;
it \nwas the age of wisdom it was the age of foolishness;it was ...'''

translation_table = str.maketrans(".,,;\n"," ")
newS = s.translate(translation_table)

newS = newS.strip()

newS = newS.lower()

count_it_was = newS.count('it was')

newS = newS.replace('was','is')

listS = newS.split()

print(f"Original string(s):{s}")
print(f"After step(a):{newS}")
print(f"After step(b):{newS}")
print(f"After step(c):{newS}")
print(f"Number of 'it was' occurrences(d):{count_it_was}")
print(f"After step(e):{newS}")
print(f"list of words(f):{listS}")