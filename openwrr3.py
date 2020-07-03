f=open("filename1.txt","w")
s="Gitam University"
f.write(s)
f.close()
f2=open("filename2.txt","w")
f1=open("filename1.txt","r")
for line in f1:
    f2.write(line)
f1.close()
f2.close()
f3=open("filename2.txt","r")
s1=f3.read()
print(s1)
f3.close()
