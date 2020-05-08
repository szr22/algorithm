# 1+2*3-4/5

def calculate(s):
    ops = []
    nums = []
    cur_num_str = ''
    for c in s:
        if c in '+-*/':
            cur_num = check_high_priority(ops, nums, cur_num_str)
            nums.append(cur_num)
            cur_num_str = ''
            ops.append(c)
        else:
            cur_num_str += c

    cur_num = check_high_priority(ops, nums, cur_num_str)
    nums.append(cur_num)
    print(ops, nums)
    while ops:
        if ops and ops[0]=='+':
            ops.pop(0)
            pre_num = nums.pop(0)
            cur_num = nums.pop(0)
            nums.insert(0, pre_num + cur_num)

        elif ops and ops[0]=='-':
            ops.pop(0)
            pre_num = nums.pop(0)
            cur_num = nums.pop(0)
            nums.insert(0, pre_num - cur_num)
    print(ops, nums)
    return nums[0]

def check_high_priority(ops, nums, cur_num_str):
    cur_num = int(cur_num_str)
    if ops and ops[-1]=='*':
        ops.pop()
        cur_num = nums.pop()*cur_num

    if ops and ops[-1]=='/':
        ops.pop()
        cur_num = nums.pop()/cur_num
    return cur_num

print(calculate('1+2*3-4/5'))