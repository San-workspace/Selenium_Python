import pytest


# @pytest.mark.usefixtures("test_setup")
# class Test_check():
#     def test_add(self):
#         print("add")
#     def test_sub(self):
#         print("sub")
#     def test_mul(self):
#         print("mul")



# @pytest.mark.usefixtures("test_setup")
# # def test_profile(dataload):
# #     print(dataload[0])

#Data load - To apply multipl test methods
@pytest.mark.usefixtures("dataload")
class Test_check2():
    def test_profile(self,dataload):

        print(dataload)

#parameerization
@pytest.mark.usefixtures("crossbrowser")
def test_crossbrowser(crossbrowser):
    print(crossbrowser[1])

