#This problem was recently asked by Google.

#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

#Bonus: Can you do this in one pass?

def problem_1(lst, k):
    diff_arr = []

    for num in lst:
        if num in diff_arr:
            return True

        diff_arr.append(k - num)
    return False


lst = [10, 15, 3, 7]
k = 17

print (problem_1(lst, k))