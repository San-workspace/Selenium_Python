file= open('test.txt')
# print(file.read()) #read all the character in the file
# print(file.read(11)) #read n no.of character in the file by passing the argument
# print (file.readline(5)) #read the file by line by line

#print the file line by line
#
# line = file.readline()
# while line!="":
#    print(line)
#    line=file.readline()

#file.readlines
for line in file.readlines():
    line=line.split()
    print(line)
# file.close()


