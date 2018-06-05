'''Q.5- Write a program to show and handle following exceptions: 
1. Import Error
2. Value Error
3. Index Error '''

l=[]
try:
    for i in range(5):
        num=int(input("Enter number:"))
        l.append(num)
    from samyak import *
    print(fact)
    print(l[5])
except ImportError:
    print("Exception",ImportError)
except ValueError:
    print("Exception",ValueError)
except IndexError:
    print("Exception",IndexError)
    
