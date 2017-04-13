# encoding=utf-8

file = open("text/diu_videotitle.txt")
n=1
for line in file:
    n=n+1
    print str(n) + " " + line.split("\t",1)[0] + " " + line.split("\t",1)[1]
