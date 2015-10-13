def insert_sort1(lists):
    length = len(lists)
    if length == 1:
        return lists
    else:
        for i in range(1, length):
            j = i - 1
            current = lists[i]
            while j >= 0:
                if current < lists[j]:
                    lists[j + 1] = lists[j]
                    lists[j] = current
                j -= 1
            print lists
        return lists
