f=open("file1.txt","w")
f.write("line number 1\n")
f.write("line number 2\n")
f.write("line number 3\n")
f.write("line number 4\n")
f.write("line number 5\n")
f.close()
f1=open("file1.txt")
number_of_lines=3
for i in range(number_of_lines):
    line=f1.readline()
    print(line)
