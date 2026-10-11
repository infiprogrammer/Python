# Write function vowelcount() that takes a string as input

vowels='aeiou'
def vowel_count(txt):
    print('a,e,i,o and u appear,respectively',end='')
    for i in vowels:
        print(txt.count(i),end=',')
    print('times')
print(vowel_count('This is govt poly hisar haryana'))