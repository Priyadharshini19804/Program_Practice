n = int(input("Enter array size: "))
arr = []
print("Enter array elements:")
for i in range(n):
    arr.append(int(input()))
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print("Sorted array:", arr)
