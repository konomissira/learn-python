def binary_search(listData, target):
    low  = 0
    high = len(listData) - 1;
    mid   = (low + high) // 2;
    while(low <= high):
        if(listData[mid] == target):
          return True;
        elif listData[mid] < target:
           low = mid + 1;
        else:
           high = mid - 1;
    
    return False;


_my_array = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
_my_target = 8

if binary_search(_my_array, _my_target):
   print(f"{_my_target} found in the array")
else:
   print(f"{_my_target} not found in the array")