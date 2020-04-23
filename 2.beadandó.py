def felbontas(n,k,r):
    db=0
    for i in range(k,n//2+1):
        if n-i in range(k,r+1):
            db+=1
    return db
print(felbontas(6,2,4))
print(felbontas(-6,-4,-2))