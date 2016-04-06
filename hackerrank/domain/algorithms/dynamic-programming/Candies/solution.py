
ratings = []
n = int(raw_input())
candy_val = [1 for x in range(n)]
for i in range(n):
    rating = int(raw_input())
    ratings.append(rating)
    if i == 0:
        prev = rating
    else:
        next = rating
        if next > prev:
            candy_val[i] = candy_val[i - 1] + 1
        prev = next
for i in range(n-1, 0, -1):
    if ratings[i-1] > ratings[i]:
        candy_val[i-1] = max(candy_val[i-1], candy_val[i]+1)
print sum(candy_val)
