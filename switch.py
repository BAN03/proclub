def switch(N, M):
    salida = [0 for i in range(N)]
    i = 2
    while i <= M:
        for j in range(N+1):
            if j % i == 0:
                if salida[j-1] == 0:
                    salida[j-1] = 1
                else:
                    salida[j-1] = 0
            
        i += 1

    return salida


if __name__ == '__main__':
    N = int(input())
    M = int(input())
    if N <= 0 or M <= 0:
        print("El numero debe ser mayor a 0")
        exit()
    if N > 1000:
        print("El primer numero debe ser menor a 1000")
        exit()
    if M > N:
        print("El segundo numero debe ser menor al primero")
        exit()
        
    print(switch(N, M))