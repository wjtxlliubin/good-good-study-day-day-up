def sorter(l, count):
    if len(l) == 1:
        return count
    else:
        MAX = -1
        MAX_ID = -1
        for index, value in enumerate(l):
            if value > MAX:
                MAX = value
                MAX_ID = index
        temp_left = l[:MAX_ID + 1]
        temp_left.reverse()
        count += 1
        temp_left.extend(l[MAX_ID + 1:])
        temp_left.reverse()
        count += 1
        # print(temp_left)
        # print(temp_left[:-1],count)
        return sorter(temp_left[:-1], count)


if __name__ == '__main__':
    print(sorter([2, 4, 3, 1], 0))
