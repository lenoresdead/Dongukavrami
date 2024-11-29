sayilar=[36,51,67,70,3,37,76,26,9,8,5,81,7,10,15,64,99,40,33,20]
for sayi in sayilar:
    if(sayi%2==0):
        print(sayi)


sayilar=[5,-70,44,65,-10,0,1,55,-7,4,30,0,-50,-1,34,-67,0,9]
poztoplam=0
negtoplam=0
sifirsayaci=0
for sayi in sayilar:
    if(sayi>0):
        poztoplam+=sayi
    elif(sayi<0):
        negtoplam+=sayi
    else:
        sifirsayaci+=1
print(poztoplam,negtoplam,sifirsayaci)
