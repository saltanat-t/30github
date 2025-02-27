def mergesort(nums1, a, nums2, b):
    i = a - 1
    j = b - 1
    k = a + b - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [4, 5, 6]
n = 3
mergesort(nums1, m, nums2, n)
print(nums1)
