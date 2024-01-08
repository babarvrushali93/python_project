#  typing speed calculator using python (while loop using)
# module name = time,string format 
#1. error(mistake()),2.speed cal(speed_time()) ,


from time import *
import random as r


# mistake
def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1
            
# speed_time
def speed_time(time_start,time_end,userinput):
    time_delay = time_end - time_start
    time_R = round(time_delay , 2)  
    speed = len(userinput)/time_R        
    return round(speed)

if __name__ == "__main__":
    while True:
       ck = input("ready to test : yes / no")
       if ck == "yes":
           test =["A paragraph is a self-contained unit of discourse in writing dealing with a particular point or idea.",
            "my name vrushali babar","welcome to wscube tech jodhpur"]

           test1 = r.choice(test)
           print("    *****typing speed*****")
           print(test1)

            # 2 line break 
           print()
           print()

           time_1 = time()
           testinput=input("Enter : ")
           time_2 = time()


           print('SPEED :', speed_time(time_1,time_2,testinput),"w\sec")
           print('ERROR :', mistake (test1 , testinput))
    
       elif ck == "no":
          print("thank you")
          break
       else:
          print( " wrong input ")
        



