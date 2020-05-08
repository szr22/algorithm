"""
Given 2 lists a and b. Each element is a pair of integers where the first integer represents
 the unique id and the second integer represents a value.
 Your task is to find an element from a and an element form b such that the sum of their values
 is less or equal to target and as close to target as possible. Return a list of ids of selected elements.
 If no pair is possible, return an empty list.

 Input:
    a = [[1, 2], [2, 4], [3, 6]]
    b = [[1, 2]]
    target = 7

    Output: [[2, 1]]

    Explanation:
    There are only three combinations [1, 1], [2, 1], and [3, 1], which have a total sum of 4, 6 and 8, respectively.
    Since 6 is the largest sum that does not exceed 7, [2, 1] is the optimal pair.
"""


def solution(a, b, target):
    # TODO: sort first
    a_dict, b_dict = {}, {}
    for key, value in a:
        a_dict[key] = value

    for key, value in b:
        b_dict[key] = value

    best = target
    best_tuple = list([])

    key_combs = [(x, y) for x in list(a_dict.keys()) for y in list(b_dict.keys())]

    for (a_key, b_key) in key_combs:
        if a_dict[a_key]+b_dict[b_key] == target:
            if best == 0:
                best_tuple.append([a_key, b_key])
            else:
                best_tuple = list([[a_key, b_key]],)
            best = target-(a_dict[a_key]+b_dict[b_key])
        elif a_dict[a_key]+b_dict[b_key] < target:
            if target-(a_dict[a_key]+b_dict[b_key]) < best:
                best = target-(a_dict[a_key]+b_dict[b_key])
                best_tuple = ([a_key, b_key])

    return best_tuple