#This problem was asked by Facebook.

#Given a binary tree, return all paths from the root to leaves.

#For example, given the tree:

#   1
#  / \
# 2   3
#    / \
#   4   5
#Return [[1, 2], [1, 3, 4], [1, 3, 5]]

def node(val, left=None, right=None):
    return {"val": val, "left": left, "right": right}

def problem_110(tree):
    arr = []
    # if node return an array with value
    if tree["left"] is None and tree["right"] is None:
        return [[tree["val"]]]
    
    # traverse left
    if tree["left"] is not None:
        arr += problem_110(tree["left"])
    
    # traverse right
    if tree["right"] is not None:
        arr += problem_110(tree["right"])
    
    # prepending node value
    for i in range(0, len(arr)):
        arr[i] = [tree["val"]] + arr[i]
    
    return arr
    
tree = node(1,
            node(2),
            node(3,
                node(4),
                node(5)
                )
            )

paths = print(problem_110(tree))
