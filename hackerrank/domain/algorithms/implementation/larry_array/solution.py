"""
Editorial
---------
Let's call inversion in sequence A (size of N) number of pairs(x,y),
where 1<=x<y<=N1 and Ax>Ay.

Let's prove that parity of inversions will not change:
A,B,C -> B,C,A.
Order of A,C changed thats +1/-1.
Order of A,Bchanged thats +1/-1.
So change is -2 or 0 or 2.

Prove that we can always get permutation:
[1,2,3,...,n-2,n-1,n] or [1,2,3,...,n-2,n,n-1].(n and n-1 are swapped).
using out operation we are
moving B and C left by one, in this way we can move 1 in first place,
then move 2 to second place and so on including n-2.
So, number of inversions will be 0([1,2,3,...,n-2,n-1,n]) or 1([1,2,3,...,
n-2,n,n-1]).
If it is 1 then it's impossible to sort, and if it's 0 that means it's sorted.

Calculate parity using any BST, solution will be O(T*Nlog2N)O(T*Nlog2N).
In this problem you can calculate answer by compairing each pair. O(T*N2)

Code:
-----
#include <bits/stdc++.h>
using namespace std;
const int N=1509;
int n;
int a[N];

void input(){
    scanf("%d",&n);
    for (int i=1;i<=n;i++)
        scanf("%d",&a[i]);
}

void sol(){
    int K=1;
    for (int i=1;i<=n;i++)
    for (int j=i+1;j<=n;j++)
        K^=(a[i]>a[j]);
    if (K) printf("YES\n");
    else printf("NO\n");
}

int main() {
    int test;
    scanf("%d",&test);
    while (test--){
        input();
        sol();
        }
    return 0;
}

"""


def rotate(l):
    # print l
    return l[1:] + l[:1]


for _ in range(int(raw_input())):
    n = int(raw_input())
    a = map(int, raw_input().split())
    # print a
    sorted_a = sorted(a)
    i = 0
    rotated = False
    while i < n:
        if i + 2 < n and (a[i] > a[i + 1] or a[i] > a[i + 2]):
            rotated = True
            l = rotate(a[i:i + 3])
            # print l
            index = 0
            for j in range(i, i + 3):
                # print j, index
                a[j] = l[index]
                index += 1
        else:
            i += 1
        if i + 1 == n and rotated:
            rotated = False
            i = 0
            # print a
    if a == sorted_a:
        print "YES"
    else:
        print "NO"
