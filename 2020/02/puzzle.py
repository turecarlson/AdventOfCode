def main():
    nums = []
    
    with open('./2020/01/input.txt') as f:
        file_contents = f.readlines()
        for each in file_contents:
            nums.append(int(each))
            
    for i in range(len(nums)):
        for j in range(len(nums)):
            for k in range(len(nums)):
                if(nums[i] + nums[j] + nums[k] == 2020):
                    print(nums[i] * nums[j] * nums[k])
                    return


if __name__ == '__main__':
    main()
