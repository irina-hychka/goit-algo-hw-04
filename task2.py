def merge_k_lists(lists):
    """
    Merge k sorted lists into one sorted list using Merge Sort.

    Parameters:
        lists (List[List[int]]): A list of sorted integer lists.

    Returns:
        List[int]: A single merged and sorted list.
    """
    if not lists:
        return []

    while len(lists) > 1:
        merged = []

        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i+1] if i+1 < len(lists) else []

            # Inline merging of two lists
            result = []
            i1 = i2 = 0
            while i1 < len(l1) and i2 < len(l2):
                if l1[i1] < l2[i2]:
                    result.append(l1[i1])
                    i1 += 1
                else:
                    result.append(l2[i2])
                    i2 += 1
            result.extend(l1[i1:])
            result.extend(l2[i2:])

            merged.append(result)

        lists = merged

    return lists[0]


# Usage:
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)