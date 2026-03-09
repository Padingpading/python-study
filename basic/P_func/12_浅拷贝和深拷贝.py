# 直接赋值:两个变量指向同一个对象,修改其中一个,就会影响另一
import copy

nums1 = [1,2,3,4,5]

# 浅拷贝:创建一个外层容器,但内部元素任然引用源对象
nums2 = copy.copy(nums1)
print(nums2)
nums2[3] = 99
print(nums2)

# 浅拷贝的问题:嵌套数据仍然共享,修改嵌套数据会互相影响
nums3 = [10,20,30,[40,50]]
nums4 = copy.copy(nums3)
nums4[3][0] = 99
print(nums3[3][0])
print(nums4[3][0])

# 深拷贝:创建一个新的容器,并递归地复制源对象中的元素
nums5 = [10,20,30,[40,50]]
nums6 = copy.deepcopy(nums5)

nums6[3][0] = 99
print(nums5[3][0])
print(nums6)