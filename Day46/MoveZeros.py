def moveZeroes(nums):
    j = 0  # Pointer for non-zero elements
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1