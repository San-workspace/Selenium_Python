# #check the cart if the item is 0 else raise the exception
#
# ItemsInCart = 0
# #
# if ItemsInCart !=2 :
#     pass
#     #raise Exception("exception error")
#
# assert (ItemsInCart != 0) #assert always expect true when it is false it fail the test and returns error
# #
# try:
#     with open('filelog.txt','r') as reader:
#         reader.read()
# except:
#     print("ERROR")
# #exception handling as py error :


try:
    file=open('test.txt','a')
    file.write('san'+'\n')
    file = open('test.txt', 'r')
    print(file.read())
except:
    print("Error")
finally:
    file.close()
    print("clean the codes")