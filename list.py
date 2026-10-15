# a = [20,40,50,60]
# print(type(a))
# a = 30
# b = a
# b = 50
# print(a)
# print(b)
# a = [1,2,3,4,5]
# b = a
# b[0] = 50
# print(a)
# print(b)
# name ="eskills"
# b = name
# b[0] ="s"
# print(b)

# b = a
# b.append(20)
# print(a)
# print(b)

a = [22,33,44,33,55]
# a.append(66)
# a.insert(2,100)
# a.extend([40,50])
# a.pop()
# b = a.index(44)
# print(b)
# a.sort()
# a.reverse()
# b = a.copy()
# b[0] = 200
# print(b)
# a.clear()
# b = a.count(33)
# print(b)


# 1. Create a List: 5 numbers ki list banao aur use print karo.
# a = [22,33,44,55,66]
# print(a)


# 2. Access Elements: List ke first aur last element ko print karo.
# a = [22,33,44,55,66]
# print(a[0], a[-1])

# 3. List Length: List me total kitne elements hain, count karo.

# def total_count(l):
#     count = 0
#     for i in l:
#         count +=1
#     return count

# result = total_count([11,22,33,44])
# print(result)

# 4. Sum of Elements: List [10, 20, 30, 40, 50] ke sabhi numbers ka sum nikalo.
# def sum(l):
#     s = 0
#     for i in l:
#         s += i
#     return s

# result = sum([10,20,30,40,50])
# print(result)


# 5. Largest Element: List [12, 45, 23, 67, 34] me sabse bada number find karo.
# def largest_el(l):
#     largest = l[0]
#     for i in l:
#         if largest < i:
#             largest = i
    
#     return largest



# result = largest_el([12, 45, 23, 67, 34])
# print(result)

# 6. Smallest Element: List [18, 5, 29, 3, 14] me sabse chhota number find karo.
# def smallest_el(l):
#     smallest = l[0]
#     for i in l:
#         if smallest > i:
#             smallest = i
    
#     return smallest



# result = smallest_el([12, 45, 23, 67, 34])
# print(result)

# 7. Add Element: Ek list banao aur user ke input se ek naya element add karo.
# def add_el(l):
#     n = int(input("Enter a number : "))
#     l.append(n)
#     return l

# print(add_el([11,22,33,44]))


# 8. Remove Element: List se kisi particular element ko remove karo.
# def remove_el(l,n):
#     l.remove(n)
#     return l

# print(remove_el([11,22,33,44],33))


# 9. Update Element: List ke second element ko change karke 100 kar do.
# def update_el(l):
#     l[1] = 100
#     return l

# print(update_el([11,22,33,44]))

# 10. Check Element: User se ek number lo aur check karo ki woh list me present hai ya nahi.
# def check_el(l):
#     n = int(input("Enter a number : "))
#     for i in l:
#         if n == i:
#             print(f"{n} exist in list")
#             break      
#     else:
#         print(f"{n} does not exist in list")

# check_el([11,22,33,44])

# Level 2: Beginner to Intermediate (11–20)
# 11. Even Numbers: List me se saare even numbers print karo.

# def even_num(l):
#     new_list = []
#     for i in l:
#         if i % 2 == 0:
#             new_list.append(i)
#     return new_list

# print(even_num([1,2,3,4,5,6,7,8,9,10,11,12,22,33]))


# 12. Odd Numbers: List me se saare odd numbers print karo.
# def odd_num(l):
#     new_list = []
#     for i in l:
#         if i % 2 != 0:
#             new_list.append(i)
#     return new_list

# print(odd_num([1,2,3,4,5,6,7,8,9,10,11,12,22,33]))

# 13. Even-Odd Count: List me kitne even aur kitne odd numbers hain, count karo.
# def count_even_odd(l):
#     even_count = 0
#     odd_count = 0
#     for i in l:
#         if i % 2 == 0:
#             even_count +=1
#         else:
#             odd_count +=1
#     return even_count , odd_count

# even,odd = count_even_odd([1,2,3,4,5,6,7,8,9,10,11])
# print(even,odd)

# 14. Positive and Negative: List me positive, negative aur zero elements ko alag-alag count karo.
# def pos_neg_zero(l):
#     pos = 0
#     neg = 0 
#     zero = 0
#     for i in l:
#         if i > 0:
#             pos +=1
#         elif i < 0 :
#             neg +=1
#         else:
#             zero +=1
#     print(f"positive num {pos} , negative num {neg} & {zero} zero")

# pos_neg_zero([11,0,2,3,4,-3,-4,55])


# 15. Reverse List: List ko reverse order me print karo.
# def rev_list(l):
#     rev = [55,33,22,11]
#     for i in range(len(l) - 1 , -1,-1):
#         rev.append(l[i])
#     return rev

# result = rev_list([11,22,33,55])
# print(result)


# 16. Sort Ascending: List ke numbers ko ascending order me arrange karo.

# def sort_ascending(l):
#     for i in range(0,len(l) - 1):
#         for j in range(i +1, len(l)):
#             if l[i] > l[j]:
#                 l[i],l[j] = l[j],l[i]
#     return l

# result = sort_ascending([11,2,66,55,4,77,3])
# print(result)
# 17. Sort Descending: List ke numbers ko descending order me arrange karo.

# def sort_decending(l):
#     for i in range(0,len(l) - 1):
#         for j in range(i +1, len(l)):
#             if l[i] < l[j]:
#                 l[i],l[j] = l[j],l[i]
#     return l

# result = sort_decending([11,2,66,55,4,77,3])
# print(result)
# 18. Count Occurrences: List [1, 2, 3, 2, 4, 2, 5] me number 2 kitni baar aaya hai, count karo.
# def count_occurance(l):
#     count = 0
#     for i in l:
#         if i == 2:
#             count +=1
#     return count

# result = count_occurance([1, 2, 3, 2, 4, 2, 5])
# print(result)


# 19. Copy a List: Ek list ki values ko doosri list me copy karo.
# def copy_list(l):
#     cpy = []
#     for i in l:
#         cpy.append(i)
#     return cpy

# result = copy_list([11,22,33,44])
# print(result)

# 20. Remove Duplicates: List [1, 2, 2, 3, 4, 4, 5] se duplicate elements remove karo.

# def remove_duplicates(l):
#     removed_items = []
#     for i in l:
#         if i not in removed_items:
#             removed_items.append(i)
#     return removed_items

# result = remove_duplicates([1,2,3,4,4,5,5,6,6,6])
# print(result)

# Level 3: Intermediate (21–30)
# 21. Second Largest: List me se second-largest number find karo.
# def sec_largest(l):
#     largest = l[0]
#     second = None
#     for i in l:
#         if i > largest:
#             second = largest
#             largest = i
#     return second

# result = sec_largest([22,3,44,5,66])
# print(result)

# 22. Second Smallest: List me se second-smallest number find karo.
# def sec_smallest(l):
#     smallest = float('inf')
#     second = float('inf')
#     for i in l:
#         if 66 < 3:
#             second = smallest
#             smallest = i
#         elif i < second and i != smallest:
#             second = i
        
#     return second



# result = sec_smallest([22,3,44,5,66])
# print(result)

