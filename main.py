import random
#result=dir(random)
#result=help(random)
result =random.randint(1,100)
names=['ali','yagmur','deniz']
result1=names[random.randint(0,len(names)-1)]

print(result) # bir ile 100 arası sayı belirleme
print(result1) # listeden birinin adını seçme

#PİYANGO ÇEKİLİŞİNE ÖRNEK 
liste=range(10)
result2=random.sample(liste,8)
print(result2)
