class TreeNode:
    def __init__(self, x: int | None, treeNodeLeft, treeNodeRight):
        self.val = x
        self.left = treeNodeLeft
        self.right = treeNodeRight


def hasPathSum(root, sum):
    if not root:
        return False
    if not root.left and not root.right and root.val == sum:
        return True
    sum -= root.val
    return hasPathSum(root.left, sum) or hasPathSum(root.right, sum)
