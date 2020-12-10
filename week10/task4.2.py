def binarySearchIterative(sequence, x):
    left = 0
    right = len(sequence)-1
    mid = 0

    while left <= right:
        mid = ((left + right) // 2)
        print('mid', sequence[mid])
        if x == sequence[mid]:
            return mid
        elif x < sequence[mid]:
            right = mid-1

        elif x > sequence[mid]:
            left = mid+1


if __name__ == "__main__":
    sample = [1, 2, 5, 6, 8, 10, 50, 70, 75, 77, 78, 79, 80, 81, 82, 85]
    x = 77
    print('Index of number ', x, 'is equal to ', binarySearchIterative(sample, x))
