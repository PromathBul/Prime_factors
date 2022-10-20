def enter (message):
    num = int(input(message))
    return num

def prime_factors (num):
    res = []
    count = 2
    while count * count <= num:
        if num % count == 0:
            res.append(count)
            num //= count
        else:
            count += 1
    if num > 1:
        res.append(num)
    return res

def list_in_text (any_list):
    output = ''
    for item in any_list:
        output += str(item) + ' '
        if not item is any_list[-1]:
            output += '* '
    return output