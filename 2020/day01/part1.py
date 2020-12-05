def main():
    nums = []

    with open("./2020/01/input.txt", "r") as f:
        file_content = f.readlines()
        for each in file_content:
            nums.append(int(each))

    for i in range(len(nums)):
        for j in range(len(nums)):
            if(nums[i] + nums[j] == 2020):
                print(nums[i] * nums[j])
                return


if __name__ == '__main__':
    main()
