# encoding=utf-8

file = open("text/diu_videotitle.txt")


lines = file.readlines(100000)
for line in lines:
    print line.split("\t",1)[0]