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
# class A():
#     def disp(self):
#         print("A disp()")
# class B(A):
#     pass
# obj = B()
# obj.disp()
class A:
    def __init__(self,x):
        self.x = x
    def count(self,x):
        self.x = self.x+1
class B(A):
    def __init__(self, y=0):
        A.__init__(self, 3)
        self.y = y
    def count(self):
        self.y += 1     
def main():
    obj = B()
    obj.count()
    print(obj.x, obj.y)
main()