

def main():

    def twoSum(nums, target):

        for i in range(len(nums)):
            if nums[i] < target:
                for j in range(i+1, len(nums)):
                    if nums[i] + nums[j] == target:
                        return ([i,j])

    result = twoSum([2, 11, 7, 15], 9)
    print(result)


if __name__ == '__main__':
	main()