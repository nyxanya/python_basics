

def rotate_string(s, t):
    i = 0
    while i < len(s):
        s = (s[1:] + s[0])
        if s == t:
            return True
            break
        i +=1
    return False

