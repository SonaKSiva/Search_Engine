from pathlib import Path
import os
f = open("stopword.txt","r")
stopword = f.read()
f.close()
path = Path('ipfile')
for file in path.glob('*.txt'):
    print(file)
    f = open(file, "r")
    doc = f.read()
    print(doc)
    newstring=''
    for word in doc.split():
        if word.upper() not in stopword.split():
            newstring = newstring+word+" "
    print("output: ", newstring)


    filename = os.path.splitext(os.path.basename(file))
    f = open('opfile/'+filename[0]+ "out.txt", "w")
    f.write(newstring)
    f.close()

path = Path('opfile')
unique =""
for file in path.glob('*.txt'):
    print(file)
    f = open(file, "r")
    doc = f.read()
    for word in doc.split():
        if word not in unique.split():
            unique = unique+word+" "
print("output1:", unique)



f = open('unique.txt', "w")
f.write(unique)
f.close()

f = open('unique.txt', "r")
newstring = f.read()
tab =[]
for word in newstring.split():
    pathlis = []
    pathlis.append(word)
    occlis = []
    for file in path.glob('*.txt'):
      f = open(file, "r")
      doc = f.read()
      count = doc.count(word)
      lisfo=[]
      lisfo.append(count)
      lisfo.append(file)

      occlis.append(lisfo)
    pathlis.append(occlis)
    tab.append(pathlis)
print(tab)
search = input("Enter the element to be search:")
stat = 0
for element in tab:


    if element[0] == search:
        stat = 1
        element[1].sort(key=lambda x:x[0], reverse = True)
        print(element[1])

        for i in range(len(element[1])):
            if element[1][i][0] !=0:
                print(element[1][i][1])
if stat == 0:
    print("Found no match")





