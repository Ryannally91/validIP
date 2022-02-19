def is_valid_IP(string):
    new_list= string.split('.') 
    if len(new_list) != 4:
        return False
    for x in new_list:
        if x.isalpha():
            return False
        if ' ' in x:
            return False
        if x[0] == '0':
            if len(x) > 1:
                return False
        if int(x) < 0 or int(x) > 255:
                    return False
    return True

print(is_valid_IP('123.045.067.089'))
