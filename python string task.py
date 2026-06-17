name=input("Enter the name:")
print("length of the string:",len(name))
print("---------------")
print("string lower:",name.lower())
print("-------------------")
print("string upper:",name.upper())
print("------------------")
print("capitalize first letter:",name.capitalize())
print("-------------------")
print("count the charecter:",name.count("a"))
print("---------------------")
position=name.find("a")
print("Display the position:",position)
print("---------------------")
text=input("Enter a word:")
print("replace the word:",text.replace("banana","apple"))
print("------------------------")
text1=input("Enter The String:")
result=text1[0:5]
if result=="hello":
    print("valid")
else:
    print("invalid")
    print("------------------------")
file=input("Enter a file name")
if file.endswith(".txt"):
    print("the file ends with .txt")
else:
    print("invalid")
print("----------------------")
name=input("Enter the name:")
print(name.strip())
name=input("Enter the name:").split()
print("split:",name)
print("-----------------------")
text=input("Enter the name")
print("join:","".join([text,"thinakaran"]))
print("----------------")
print("count charecter:",len(text))
print("--------------------")
result=text[::-1]
print("reverse:",result)
if text==result:
    print("palindrome")
else:
    print("consonant")
    print("-------------")
result=text.isalpha()
print("alphabet:",result)
print("---------------")
num=text.isdigit()
print("number:",num)
print("-----------------------")
name=input("Enter the name:")
name=name.lower()
count=(
     name.count('a')+
     name.count('e')+
     name.count('i')+
     name.count('o')+
     name.count('u')
     )
print("numbers of vowels",count)
print("---------------------")
text=input("Enter the text").lower()
print("The lower text is:",text)
print("----------")
print(text)
print("capitalize each word:",text.title())
print("-------------")








