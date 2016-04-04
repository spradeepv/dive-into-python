"""
Larry has a permutation of N numbers, AA, whose unique elements range from
1 to N (i.e.: A={a1,a2,...,aN-1,aN}. He wants A to be sorted,
so he delegates the task of doing so to his robot. The robot can
perform the following operation as many times as it wants:

Choose any 3 consecutive indices and rotate their elements in such a way
that ABC rotates to BCA, which rotates to CAB, which rotates back
to ABC.
For example: if A={1,6,5,2,4,3} and the robot rotates (6,5,2), A becomes
{1,5,2,6,4,3}.

On a new line for each test case, print YES if the robot can fully sort
A; otherwise, print NO.

Input Format
------------
The first line contains an integer, T, the number of test cases.
The 2T subsequent lines each describe a test case over 2 lines:

An integer, NN, denoting the size of A.
N space-separated integers describing A, where the ithith value describes
element ai.

Constraints
-----------
1<=T<=10
3<=N<=1000
1<=ai<=N, where every element ai is unique.

Output Format
-------------
On a new line for each test case, print YES if the robot can fully sort
A; otherwise, print NO.

Sample Input
------------
3
3
3 1 2
4
1 3 4 2
5
1 2 3 5 4

Sample Output
-------------
YES
YES
NO

Explanation
-----------
In the explanation below, the subscript of A denotes the number of
operations performed.

Test Case 0:
------------
A0={3,1,2}->rotate(3,1,2)->A1={1,2,3}
A is now sorted, so we print YES on a new line.

Test Case 1:
------------
A0={1,3,4,2}->rotate(3,4,2)->A1={1,4,2,3}.
A1={1,4,2,3}->rotate(4,2,3)->A2={1,2,3,4}.
A is now sorted, so we print YES on a new line.

Test Case 2:
------------
No sequence of rotations will result in a sorted AA. Thus, we print NO on
a new line.

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
