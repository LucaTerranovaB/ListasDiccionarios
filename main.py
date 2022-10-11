#Terranova Luca

# TP LIstas Disccionarios


def rep(arr):

    result = {}

    for n in arr:
        if n in result:
            result[n] += 1
        else: 
            result[n] = 1
    return result

if __name__=='__main__':
    n = int(input(print("Insert a number:  ")))
    print(rep(n))