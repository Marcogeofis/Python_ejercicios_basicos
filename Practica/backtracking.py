def encontrar_permutacion(nums):
    def backtrack(perm):
        print(len(perm), len(nums))
        if len(perm) == len(nums):
            result.append(perm[:])
            return
        
        for num in nums:
            if num not in perm:
                perm.append(num)
                backtrack(perm)
                perm.pop()
    
    result = []
    backtrack([])
    return result


if __name__ == '__main__':
    nums = [1,2,3]
    permutaciones = encontrar_permutacion(nums)
    for perm in permutaciones:
        print(perm)