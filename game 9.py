rules=input("read the rules? y/n ")
if rules==("y") or rules==("Y") :
  print ("  1) Two players take turns") 
  print ("  2) During a turn a player can remove only 1 or 2 adjacent numbers")
  print ("  3) The player who removes the last number wins \n")

while True :

 print ("enter 1 for player vs player")
 print ("enter 2 for player vs AI")
 
 
 mode=int(input())
 if mode<1 or mode>2 :
   print ("only choose 1 or 2 \n")
   continue
   
   
 import random
 tokens=[]
 p=[]
 size=random.randint(10,30)
 
 
 print ("\n")
 for s in range (1,size+1) :
   tokens.append(s)
   print (s,end=" ")
 print ("\n")
 
 
 i=1
 r=size
 d=3
 n=1
 
 
 while i<=size :
  if mode==1 or (mode==2 and i%2!=0) :
    if i%2!=0 and mode==1 :
      print ("\nplayer 1's turn :: ")
    if i%2==0 and mode==1 :
      print ("\nplayer 2's turn :: ")
    if i%2!=0 and mode==2 :
      print ("\nplayer's turn :: ")
      
      
    while n!=0 : #removing numbers in any mode
      if r==1 : n=1
      else : n=int(input("do you want to choose 1 or 2 numbers ? "))
      while n<1 or n>2 :
        print ("you can only choose 1 or 2 numbers")
        n=int(input())
        
      if n==1 : #removing 1 number
        if r==1 : x=int(input("enter the last number : \n"))
        else : x=int(input("Enter the number : \n"))
        if (x<1 and x>size) or (x in p) :
          print ("The number is not valid \n")
          continue
        else :
          tokens[x-1]=("_")
          r-=1
          p.append(x) 
        break
        
      if n==2 : #removing 2  numbers
        x=int(input("Enter first number : \n"))
        y=int(input("Enter second number : \n"))
        if (x<1 and x>size) or (x in p) or(y<1 and y>size) or (y in p) or (y==x) or (y<x-1) or (y>x+1) :
          print ("The numbers are not valid together \n")
          continue
        tokens[x-1]=("_")
        tokens[y-1]=("_")            
        p.append(x)
        p.append(y)
        r-=2
        break
        
        
    if mode==1 :
      print ("__________________________________________\n")
      for token in tokens : print (token,end=" ")
      print ("\n")
      
      
  if i%2==0 and mode==2 : #removing numbers in AI mode
    print ("\nAI's turn :: ")
    c=d
    while c!=0 :
      for k in range (0,size,1) : #win strategy
        if c==3 :
         if tokens[k]!=("_") and tokens[k+1]!=("_") and tokens[k+2]!=("_") and k<(size-2) :
          tokens[k+1]=("_")
          p.append(k+2)
          print (k+2)
          r-=1
          c=0
          if r%2!=0 :
            tokens[k+2]=("_")
            p.append(k+3)
            print (k+3)
            r-=1
         if k==(size-3) : d=2
         if k<(size-3) :
            continue
         else :
            d=2
            break
            
        if c==2 :
         if tokens[k]!=("_") and tokens[k+1]!=("_") and k<(size-1) :
          tokens[k]=("_")
          p.append(k+1)
          print (k+1)
          r-=1
          c=0
          if r%2!=0  :
            tokens[k+1]=("_")
            p.append(k+2)
            print (k+2)
            r-=1
         if k==(size-2) : d=1
         if k<(size-2) : continue
         else :
            d=1
            break
            
        if c==1 and tokens[k]!=("_") :
           tokens[k]=("_")
           p.append(k+1)
           print (k+1)
           r-=1
           c=0
           break
      if c!=0 :
        c-=1
        continue
        
        
    print ("__________________________________________\n") 
    for token in tokens : print (token,end=" ")
    print ("\n")
    
    
  if r==0 : #showing the winner
    if i%2!=0 and mode==1 :
      print ("\nplayer 1 wins\n")
    if i%2==0 and mode==1 :
      print ("\nplayer 2 wins\n")
    if i%2!=0 and mode==2 :
      print ("\nplayer wins\n")
    if i%2==0 and mode==2 :
      print ("\nAI wins\n")
    i=111
    
  i+=1
  
  
 play=str(input("Do you want to play again ? y/n \n")) 
 if play==("y") or play==("Y") :
   print ("\n") 
   continue
 else : break