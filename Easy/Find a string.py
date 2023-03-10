def count_substring(string, sub_string):
    s = ""
    result = 0
    for i in range(len(string)-1) :
        s += string[i]
        result += s.count(sub_string)
    return result
    
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)