class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        
        # check if it is a leaf node
        if not root.left and not root.right:
            return targetSum == root.val
        
        targetSum -= root.val
        
        return (self.hasPathSum(root.left, targetSum) or
                self.hasPathSum(root.right, targetSum))