# here both list.pop() and list.append() 
# both have time complexity O(1)
# sorting takes nlogn
# overall time complexity: O(n*nlogn) !!!!
# need to improve.


def lastStoneWeight(stones):
    stones = sorted(stones)
    while len(stones) >= 2:
        last = stones.pop()
        last_prev = stones.pop()
        # print(f'last: {last} last_prev: {last_prev}')
        if last != last_prev:
            new_weight = last - last_prev
            # print(f'new_wieight: {new_weight}')
            stones.append(new_weight)
        stones = sorted(stones)
    return stones[0] if len(stones) else 0