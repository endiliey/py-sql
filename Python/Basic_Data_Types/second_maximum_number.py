if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    my_list = list(arr)
    z = max(my_list)
    while(z == max(my_list)):
        my_list.remove(z)
        
    print(max(my_list))
