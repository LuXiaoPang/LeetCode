#!/bin/python3
#=============================================================================
# Author          : luzhanzhao
# Email           : zhanzhao.lu@corerain.com
# Last modified   : 2019-08-20 10:54
# Filename        : RemoveElement_v1.py
# Description     : 
#=============================================================================
def RemoveElement(nums,val):
    for i in range(len(nums)):
        while nums[i]==val:
            del nums[i]
            if i>=len(nums)-1:
                break
        if i>=len(nums)-1:
            break
    return len(nums)

a = RemoveElement([3,1,3,3,4,5,3],3)
print(a)
