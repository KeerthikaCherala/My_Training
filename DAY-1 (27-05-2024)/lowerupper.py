'''for checking we use i.islower() and i.isupper() to convert we use i.upper(),i.lower()'''
str=input()
s=''
for i in str:
    if(i in 'AEIOU' or i in 'aeiou'):
        i=i.upper()
        s=s+i
    else:
       i=i.lower()
       s=s+i
print(s)
        