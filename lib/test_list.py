
# -*- coding: UTF-8 -*-

# def login(username="jackwu" ,passwd="123"):
#     if(username is "admin" and passwd is "123"):
#         print "success"
#     else: 
#        print "login fail"
      
def login(username="jakcwu",passwd="123"):
           if (username is "jackwu" and passwd is "123" ):
               print "success"
           else:
               print "fail"

def login_list(*info):
           username=info[0];
           passwd=info[1];
           if (username is "jackwu" and passwd is "123" ):
               print "success"
           else:
               print "fail"
               

def  login_key(**info)：
         keys=info.keys()
         username=''
         passwd=''
         for key in keys:
             if key=='username':
                 username=info[keys]
             elif key=='passwd':
                 passwd=info[keys]

        if username is "jackwu" and passwd is "123":
            print "success"
        else:
            print "fail"                 


#打包输出结果

def max(*info):
    if(info[0]>info[1]):
        return info[0]
    else :
        return info[1]



def main():
    //login_key(username="jackwu",passwd="123")
    a=raw_input("input:a=")
    
    max()

if __name__ == '__main__':
    main()

