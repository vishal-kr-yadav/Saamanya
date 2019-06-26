a = [12,11,13,5,6]

for i in range(0,len(a)):
    j=i+1

    if a[j] < a[i] :
        a[j],a[i]=a[i],a[j]
    break
print(a)