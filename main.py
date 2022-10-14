t = int(input())

for i in range(t):
    nums1 = list(map(int, input().split()))
    m = int(input())
    nums2 = list(map(int, input().split()))
    n = int(input())
    for get in range(len(nums1) - 1, m - 1, -1):
        nums1.pop(get)
    for check in range(len(nums2)):
        nums1.append(nums2[check])
    nums1.sort()
    print(nums1)