# -*- coding: UTF-8 -*-



class animal(object):
  
   def __str__(self):
       pass

class dog(animal):
    
    def  __init__(self):
        self.__type="dog"
    def   gettype(self):
        return self.__type
    def __str__(self):
        print "this animal is %s" %self.gettype()


class pig(animal):
    def __init__(self):
        self.__type="pig"
    def gettype(self):
        return self.__type

      def __str__(self):
        print "this animal is %s" %self.gettype()


class factory(object):
    animal={}#key value
    animal["dog"]=dog()
    animal["pig"]=pig()
    def createanimal(self,type):
        if type in self.animal:
            return self.animal[key]
        else:
            return 


def main():
    op=raw_input("animal type=")
    f=factory()
    f.createanimal(op)
    
if __name__ == '__main__':
    main()
