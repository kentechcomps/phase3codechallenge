

def positivenofunction (a, b, c,):
    posiitivenocount = 0
    if a > 0:
        posiitivenocount +=1
    if b > 0 :
        posiitivenocount +=1
    if c > 0 :
        posiitivenocount +=1

    return posiitivenocount == 2

print (positivenofunction(-1 ,2 ,-2))