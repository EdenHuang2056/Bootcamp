
def main():

    def maxProduct(nums):
    # 請用你的程式補完這個函式的區塊
        max = 0
        a = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                a = nums[i]*nums[j]
                if i == 0 and j == 1:
                    max = a
                if a > max:
                    max = a

        print(max)



    maxProduct([5, 20, 2, 6])
    # 得到 120 因為 20 和 6 相乘得到最大值

    maxProduct([10, -20, 0, 3])
    # 得到 30 因為 10 和 3 相乘得到最大值


if __name__ == '__main__':
	main()
