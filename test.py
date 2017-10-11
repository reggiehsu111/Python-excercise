def mystery(N):
    if (N>0):
        print(N)
        mystery(N-2)
    else:
        print(N)
        if (N>-1):
            mystery(N+1)
mystery(2)