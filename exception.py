def fun(l,ind):
    try:
        a=l.copy()
        a[0]=l[0]/l[ind]
    except ValueError:
        print("value error")
    finally:
        print("end of fun")
    
