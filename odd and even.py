x=input()
l=x.split()
i=1
j=0
while(j<len(l)):
    if i%2==0:
        print(l[j],end="")
        i=i+2
        j=j+1
i=2
j=0
while(j<len(l)):
      if i%2==0:
          print(l[j],end='')
          i=i+2
