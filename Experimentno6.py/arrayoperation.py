arr = [10, 20, 30, 40, 50]

print("Original Array:", arr)


print("Element at index 2:", arr[2])

arr.insert(2, 25)
print("After Insertion:", arr)

arr.append(60)
print("After Appending:", arr)

arr.remove(30)
print("After Deletion:", arr)

arr[0] = 100
print("After Updating:", arr)

if 40 in arr:
    print("Element 40 found")
else:
    print("Element 40 not found")

arr.sort()
print("Sorted Array:", arr)
print("Length of Array:", len(arr))

arr.reverse()
print("Reversed Array:", arr)