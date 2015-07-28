#encoding:utf8

str='asdfghjklasdfg'
strT = range(0,len(str))
for i in range(0,len(str)):
    strT[i] = str[i]
for i in range(0,len(str)-1):
    for j in range(i+1,len(str)):
        if strT[i] == strT[j]:
            strT[i] = '1'
            strT[j] = '1'
            
print strT
for i in range(0, len(str)-1):
    if strT[i] != '1':
        print strT[i]      
        break  


