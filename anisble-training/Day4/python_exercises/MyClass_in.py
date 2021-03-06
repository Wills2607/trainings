#!/usr/bin/pyth

class Parent:
      
       def __init__ (self):
          print ("Inside constructor")
          self.__privateData = 100
          self._protectedData = 200
          self.publicData = 300
          
       def setValues(self,val1, val2, val3):
         self.__privateData = val1
         self._protectedData = val2
         self.publicData = val3

       def printValues(self):
         print ("Value of private data is  " + str (self.__privateData))
         print ("Value of protected data is  " + str (self._protectedData))
         print ("Value of public data is  " + str (self.publicData))

class Child(Parent):
      def __init__(self):
          Parent.__init__(self)
          self.data = 100
   
def main():
      obj1 = Child()
      print("Value of member variables before calling SetValues function")
      obj1.printValues()
      obj1.setValues(500,600,700)
      print("Value of meber variables before calling SetValues function")
      obj1.printValues()
    
      print ("Attempt to read public varibale directly", obj1.publicData) 
      print ("Attempt to read protected varible directly", obj1._protectedData) 
      print ("Attempt to read private directly", obj1.__privateData) 

main()
