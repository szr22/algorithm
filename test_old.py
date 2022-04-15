def print_boxed_text(input_str):
    words = input_str.split(" ")
    max_len = max(list(map(len, words)))
    print("*" * (max_len+4))
    for word in words:
        print("* " + word + " *")
    print("*" * (max_len+4))

print_boxed_text('hello world')



def cellCompete(states, days):
    n= len(states)
    next_states = [0] * n
    for _ in range(days):
        states = [0]+states+[0]
        for i in range(n):
            if states[i] == states[i+2]:
                next_states[i] = 0
            else:
                next_states[i] = 1
        states = next_states
        print(next_states)
    return next_states

cellCompete([1,0,0,0,0,1,0,0],1)
cellCompete([1,1,1,0,1,1,1,1],2)

def generalizedGCD(num, arr):
    cur = find_gcd(arr[0], arr[1])
    for i in range(2, len(arr)):
        cur = find_gcd(cur, arr[i])
    return cur

def find_gcd(num1, num2):
    if num1 > num2:
        find_gcd(num2, num1)

    if num2%num1 == 0:
        return num1
    else:
        return find_gcd(num2%num1, num1)

generalizedGCD(5, [-18,4,8,56])