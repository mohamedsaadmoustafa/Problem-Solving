def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        foo = string[i:i+k]
        # remove dublicates and save order 
        result = "".join(dict.fromkeys(foo))
        print(result)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
