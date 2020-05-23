def reads():  
 file2 = open("data1.txt","r+")  
 j=None 

  
 k=file2.readlines()
 for j in k:
    print(j)
 if j==None:
    print("none")
 file2. truncate(0)    
 file2.close()
reads() 