
def main():

    def maxProduct(nums):
    # 請用你的程式補完這個函式的區塊
        a = 0
        b = 0

        for i in range(len(nums)):
            if nums[i] > b:
                b = nums[i]

                if b > a:
                    b = a
                    a = nums[i]

        print(int(a*b))

    maxProduct([5, 20, 2, 6])
    # 得到 120 因為 20 和 6 相乘得到最大值

    maxProduct([10, -20, 0, 3])
    # 得到 30 因為 10 和 3 相乘得到最大值


if __name__ == '__main__':
	main()