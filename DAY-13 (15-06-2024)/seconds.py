n=int(input())
h=n//3600
s=n-(3600*h)
m=s//60
sec=s-(m*60)
print(f"{h}hrs {m}mins {sec}s")