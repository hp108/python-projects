def neighbours(sx,sy,m,n):
    l=[]
    if(sx-2>=0 and sy+1<n):
        l.append((sx-2,sy+1))
    if(sx-2>=0 and sy-1>=0):
        l.append((sx-2,sy-1))
    if(sx+2<m and sy+1<n):
        l.append((sx+2,sy+1))
    if(sx+2<m and sy-1>=0):
        l.append((sx+2,sy-1))
    if(sx-1>=0 and sy-2>=0):
        l.append((sx-1,sy-2))
    if(sx+1<m and sy-2>=0):
        l.append((sx+1,sy-2))
    if(sx-1>0 and sy+2<n):
        l.append((sx-1,sy+2))
    if(sx+1<m and sy+2<n):
        l.append((sx+1,sy+2))
    return l
    
def knight(marked_indices,sx,sy,tx,ty,m,n):
    marked_indices=[[0 for _ in range(m)] for _ in range(n)]
    if(m==0 and n==0 and sx==0 and sy==0 and dx==0 and dy==0):
        return 1
    marked_indices[sx][sy]=1
    queue=[(sx,sy)]
    while queue != []:
        (ax,ay)=queue.pop()
        for [ax,ay] in list(neighbours(ax,ay,m,n)):
            if(marked_indices[ax][ay]!=1):
                marked_indices[ax][ay]=1
                queue.insert(0,(ax,ay))
    return marked_indices[tx][ty]

print("welcome to KNIGHTL game")
while True:
    try:
        print("enter starting indices")
        sx=int(input("enter 1st index of starting indices:- "))
        sy=int(input("enter 2nd index of starting indices:- "))
        dx=int(input("enter 1st index of destination indices:- "))
        dy=int(input("enter 2nd index of destination indices:- "))
        m=int(input("enter no of rows:- "))
        n=int(input("enter no of columns:- "))
    except:
        print("enter data correctly")
    else:
        break
    
while True:
    marked_indices=[[0 for _ in range(m)] for _ in range(n)]
    ans=knight(marked_indices,sx,sy,dx,dy,m,n)
    if(ans):
        print("starting indices can reach the destination indices")
    else:
        print("starting indices can not reach the destination indices")
    print()
    print()
    s=input("Enter Yes to play another time:- ")
    if(s.upper()!="YES"):
        break
        

                
        