"""
Devu is working hard to manage his diet. Each day, he both consumes and
burns a certain number of calories.

Devu keeps N days of calorie data in 2 arrays of size N: array C (
calories consumed) and array B (calories burned). He wants to know the
number, k, of index ranges [l,r] such that:
C[l]+C[l+1]+...+C[r]>=B[l]+B[l+1]+...+B[r], where 0<=l<=r<=N-1
Help Devu find k, then print it on a new line.

Input Format

The first line contains an integer, N, denoting the number of days tracked
in C and B.
The second line contains N space-separated integers describing array C.
The third line contains N space-separated integers describing array B.

Constraints

1<=N<=2*10e5
0<=C[i]<=10e9
0<=B[i]<=10e9

Output Format

Print k on a new line.

Sample Input

3
1 2 3
3 2 1
Sample Output

4
Explanation

C={1,2,3} B={3,2,1}
The following [l,r] ranges satisfy the requirements in the problem
statement:

[0,2]: C[0]+C[1]+C[2] >= B[0]+B[1]+B[2] => 1+2+3 >= 3+2+1 => 6>=6
[1,2]: 2+3>=2+1-> 5>=3
[1,1]: 2>=2
[2,2]: 3>=1
Thus, k=4, so we print 4 on a new line.
"""
res=[]
def msort(L):
    if(len(L)==1):
        return L
    else:
        temp1=msort(L[:len(L)//2])
        temp2=msort(L[len(L)//2:])
        return merge(temp1,temp2)
def merge(L,M):
    temp=[]
    l1,l2=len(L),len(M)
    pos1,pos2,count=0,0,0
    while(count<(l1+l2)):
        if(pos1<l1 and pos2<l2):
            if(L[pos1]<=M[pos2]):
                temp.append(L[pos1])
                count+=1
                pos1+=1
                res.append(pos2)
            else:
                temp.append(M[pos2])
                count+=1
                pos2+=1
        elif(pos1<l1):
            temp.append(L[pos1])
            count+=1
            pos1+=1
            res.append(pos2)
        else:
            temp.append(M[pos2])
            count+=1
            pos2+=1
    return temp

res = []
n = int(input())
c = [int(i) for i in raw_input().split()]
b = [int(i) for i in raw_input().split()]
c1 = [0 for i in range(n+1)]
c2 = [0 for i in range(n+1)]

for i in range(1,n+1):
    c1[i] = c[i-1] + c1[i-1]
    c2[i] = b[i-1] + c2[i-1]

print c1
print c2

l = [0 for i in range(n+1)]

for i in range(n+1):
    l[i] = c1[i] - c2[i]
print l
temp=msort(l)
print res
ans = sum(res)
ans = (n*(n+1))//2 - ans
print(ans)