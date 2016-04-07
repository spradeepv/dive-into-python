n, k = map(int, raw_input().split())
problems_in_chapter = map(int, raw_input().split())
page_no = 1
special_problems = 0
for i in problems_in_chapter:
    index = 0
    for j in range(1, i+1):
        #print i, page_no, j
        if page_no == j:
            special_problems += 1
        index += 1
        if index % k == 0:
            page_no += 1
    if index % k != 0:
        page_no += 1
print special_problems