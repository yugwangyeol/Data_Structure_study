def hanoiTower(n,fr,tmp,to):
    if (n==1):
        print("Disk %d : %s -> %s"%(n,fr,to))
    else:
        print(n)
        hanoiTower(n-1,fr,to,tmp)
        print("Disk %d : %s -> %s"%(n,fr,to))
        hanoiTower(n-1,tmp,fr,to)

hanoiTower(4,'A','B','C')
# H
