import heapq

def merge_k_sorted_lists(lists):
    min_heap = []
    merged_list = []

    for list_index, lst in enumerate(lists):
        if lst:  
            heapq.heappush(min_heap, (lst[0], list_index, 0))  
    while min_heap:
        smallest, lst_idx, elem_pos = heapq.heappop(min_heap)
        merged_list.append(smallest)

        if elem_pos + 1 < len(lists[lst_idx]):
            next_elem = lists[lst_idx][elem_pos + 1]
            heapq.heappush(min_heap, (next_elem, lst_idx, elem_pos + 1))

    return merged_list


# Example 
arrays_a = [
    [1, 3, 5, 7],
    [2, 4, 6, 8],
    [0, 9, 10, 11]
]
arrays_b = [
    [1, 3, 7],
    [2, 4, 8],
    [9, 10, 11]
]

print(merge_k_sorted_lists(arrays_a))
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print(merge_k_sorted_lists(arrays_b))
# Output: [1, 2, 3, 4, 7, 8, 9, 10, 11]
