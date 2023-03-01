
#file =open('test.txt','a') #open the file in append mode
#file.write('def'+'\n') #adding 'def' at last
#print(file)
#file.close()

with open('test.txt','r') as reader:
    list1=reader.readlines()
    reversed(list1)
    with open('test.txt','w') as writer:
       for i in reversed(list1):
          writer.write(i)
          print(i)
