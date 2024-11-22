def rotation(t,k):
    c = t
    l=len(c)
    u=[]
    if k>=0:
        if l>k:
            while l>k:
                u+=c[k:k+1:1]
                c.pop(k)
                l=len(c)
            while l>0:
                u+= c[0:1:1]
                c.pop(0)
                l=len(c)
            u+= c
        if l<k:
            while l>0:
                u+= c[0:1:1]
                c.pop(0)
            u+= c
    if k<0:
        m=l+k
        if l>m:
            while l>m:
                u+=c[m:m+1:1]
                c.pop(m)
                l=len(c)
            while l>0:
                u+= c[0:1:1]
                c.pop(0)
                l=len(c)
            u+= c
        if l<m:
            while l>0:
                u+= c[0:1:1]
                c.pop(0)
            u+= c
    print(u)

rotation ([1,2,3,4,5], 2)
rotation ([1,2,3,4,5], -3)
rotation ([1,2,3,4,5,7,8,4,6,7], 2)
rotation ([1,2,3,4,5,7,8,4,6,7], -8)
