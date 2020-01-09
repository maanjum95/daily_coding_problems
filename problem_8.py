#This problem was asked by Google.

#A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

#Given the root to a binary tree, count the number of unival subtrees.

#For example, the following tree has 5 unival subtrees:

#   0
#  / \
# 1   0
#    / \
#   1   0
#  / \
# 1   1

def node(val, left=None, right=None):
    return {"val": val, "left": left, "right": right}

def problem_8(tree):
    l_sum = None
    r_sum = None
    l_val = None
    r_val = None

    # if it is a leaf
    if tree["left"] is None and tree["right"] is None:
        return [tree["val"], 1]
    
    # traverse left side of the tree
    if tree["left"]:
        [l_val, l_sum] = problem_8(tree["left"])
    
    # traverse right side of the tree
    if tree["right"]:
        [r_val, r_sum] = problem_8(tree["right"])
    
    # compare values traversed up the tree
    if l_val and r_val and l_val == r_val == tree["val"]:
        return [tree["val"], l_sum + r_sum + 1]
    else:
        return [None, l_sum + r_sum]
    



tree = node(0, 
        node(1),
        node(0, 
            node(1, 
                node(1), 
                node(1)
                ), 
            node(0)))

print(problem_8(tree)[1])