# -*- coding: UTF-8 -*-



class animal(object):
    name=""
    def __init__(self,__name):
         self.name=__name
    def setname(self, _name):
        self.name=_name
    
    def getname(self):
         return self.name


def max(a,b):
    if a>b:
      return a;
    else:
        return b;

def main():
    print max(1,2);

def rlogin():
    name=raw_input("name:");
    passwd=raw_input("passwd:");
    if(name is str("jackwu") and passwd is str("123")):
        print "success"
    else:
        print "failed"

if __name__ == '__main__':
    rlogin();