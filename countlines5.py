fname="file1.txt"
count=0
with open(fname,"r") as f:
    for line in f:
        count+=1
print("Total number of lines is",count)
