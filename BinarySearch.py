#Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
class BinarySearch(object):
    def searchInsert(self, nums, target):
       
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start=0
        end = len(nums) - 1
         

        while(start<=end):
            mid=start + (end - start)//2

            if (nums[mid] == target):
                print (mid)
                break
            
            elif(nums[mid]<target):
                start=mid+1

            else:
                end=mid-1

        print (start)

    nums = [1, 3, 5, 6]
    target = 5

    obj = BinarySearch()
    obj.searchInsert(nums, target)