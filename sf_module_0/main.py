import random

# ищем число secret в диапозоне от nf до nt
def search(nf,nt):

    count=1

    while True:
        num = round( (nf+nt)/2 )

        if secret > num:
            nf=num+1
        else:
            nt=num-1

        if secret==num or secret==nf or secret==nt:
            print("Found "+str(secret)+" ! Count = "+str(count))
            exit()

        count += 1
        print(str(count) + ": "+str(nf)+".."+str(nt))
        

secret = random.randint(1,100)

print("secret=" + str(secret) )

search(1,100)
