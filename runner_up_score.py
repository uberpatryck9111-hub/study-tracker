if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    unique_nums = set(arr)
    
    sorted_nums = sorted(unique_nums)
    
    print (sorted_nums[-2])