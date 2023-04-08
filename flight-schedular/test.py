# # def fn(x):
# #          try:
# #              print(5/x)
# #          except:
# #              print('Error occurred')
# # fn(0)
# def fn(x):
#     try:
#         print(5/x)
#     except ZeroDivisionError:
#         print("Except block")
#     else:
#         print("Else block")
#     finally:
#         print("Finally block")
# fn(0)
class A():
    def disp(self):
        print("A disp()")
class B(A):
    pass
obj = B()
obj.disp()
