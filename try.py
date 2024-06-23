import random
maze=[]
def generate_path(N, M):
    maze = []
    for i in range(N):
        row = []
        for j in range(M):
            row.append(0)
        maze.append(row)
        print(maze)
    # your code here

    maze[0][0]=2
    m=0
    n=0
    new_path=[]
    print(N,M)
    while True:
        choose=[]
        new_path.append([m,n])
        if m<N-2:
            choose.append([m+1,n])
        elif m==N-1 and n<M-1:
            choose.append([m,n+1])
        if n<M-1:
            choose.append([m,n+1])
        elif n==M-1 and m<N-1:
            choose.append([m+1,n])
        print(choose)
        c=random.choice(choose)
        print(c)
        if c ==[m+1,n]:
            m+=1
            maze[m][n]=2
        elif c ==[m,n+1]:
            n+=1
            maze[m][n]=2
        if maze[N-1][M-1]==2:
            break
        print(m,n)

    return maze
a=int(input('1'))
b=int(input('1'))
generate_path(a,b)
print(maze)