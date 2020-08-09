import sys

def count_routers(houses, gap):
    count = 1
    temp = houses[0]
    N = len(houses)
    for i in range(1, N):
        if houses[i] - temp >= gap:
            temp = houses[i]
            count += 1
    return count
            

if __name__ == "__main__":
    N, C = sys.stdin.readline().split(" ")
    N = int(N)
    C = int(C)
    
    houses = []
    for _ in range(N):
        houses.append(int(sys.stdin.readline()))
    
    houses.sort()

    min_gap = houses[1] - houses[0]
    max_gap = houses[N - 1] - houses[0]
    
    while True:
        mid = (max_gap + min_gap) // 2
        count_by_mid = count_routers(houses, mid)

        if count_by_mid < C:
            max_gap = mid - 1
        elif count_by_mid > C:
            min_gap = mid + 1
        else:
            result = mid
            break

    print(result)
        


# We can search an element on sorted list by STL binary search
'''

import bisect
mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect.bisect(mylist, 3))

'''
