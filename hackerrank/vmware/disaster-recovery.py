"""
Problem Statement

Mimmy is managing company X's datacenters. So it is most unfortunate that a
power outage took down one of their datacenters. Mimmy called the power
supply company and it turns out the outage will not be fixed in the near
future. Typically companies have disaster recovery set up for such cases but
company X wanted to cut the extra costs. So Mimmy will have to move all the
servers from the datacenter to a backup datacenter by hand.

The servers in the datacenter are ordered in line. Mimmy can move either the
first or the last server in the line but she can't reach any other server.
In one hour Mimmy comes, takes one server to the backup datacenter, sets it
up and starts it. Thus every hour Mimmy will "rescue" either the first or
the last of the remaining servers. Each server si has an associated downtime
cost di - the amount of money that company X will lose every hour that si is
down.

Mimmy wants to minimize the costs for company X. She knows all the downtime
costs of the servers in the datacenter and she wants to device an optimal
way to move them. Help her by writing a program that will find the minimal
loss for company X.

Input Format

The first line of the input contains a single integer N(1 <= N <= 1000) -
the number of servers in the datacenter Mimmy has to recover. The next line
contains N integer numbers di(1 <= di <= 100000)- the downtime costs of the
servers in the same order that the servers are placed in the line. The
downtime costs are separated by a single space.

Output Format

Output a single number - the minimal loss for company X, for which Mimmy can
move all the servers.

Sample Input

4
5 1 4 3

Sample Output

27

Explanation

In the first hour Mimmy will save s1(downtime cost 5), in the second hour
she will save s4(d4=3), then she will save the s3(d3=4) and lastly she will
save s2(d2=1). The overall cost for the company will be 5 * 1 + 3 * 2 + 4 *
3 + 1 * 4 = 27
"""

def get_index_to_remove(l):
    if l:
        last_index = len(l) - 1
        first = l[0]
        last = l[last_index]
        if first == last:
            return get_index_to_remove(l[1:len(l)-1])
        if first > last:
            return 0
        else:
            return 1
    else:
        return 0


n = int(raw_input())
down_time_costs = map(int, raw_input().split())
time = 1
loss = 0
while down_time_costs:
    first = down_time_costs[0]
    last = down_time_costs[len(down_time_costs) - 1]
    if first == last and len(down_time_costs) > 2:
        index = get_index_to_remove(list(down_time_costs[1:len(down_time_costs)-1]))
        if index:
            loss += last * time
            down_time_costs.pop(len(down_time_costs) - 1)
        else:
            loss += first * time
            down_time_costs.pop(0)
    else:
        first_now = first * time
        first_next = first * (time + 1)
        last_now = last * time
        last_next = last * (time + 1)
        if first_now > last_now and first_next > last_next:
            loss += first * time
            down_time_costs.pop(0)
        else:
            loss += last * time
            down_time_costs.pop(len(down_time_costs) - 1)
    time += 1
print loss