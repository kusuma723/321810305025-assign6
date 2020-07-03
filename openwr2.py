f=open("file1.txt","w")
s="Hello good morning to everyone"
f.write(s)
print(s)
f.close()
f1=open("file1.txt","a")
t="Have a nice day"
f1.write(t)
print(t)
f1.close()
