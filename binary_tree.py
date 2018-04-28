class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def serialize(root):
    res = []
    node_queue = [root]
    while node_queue:
        node = node_queue.pop(0)
        if node == None:
            res.append('#')
        else:
            res.append(str(node.val))
            node_queue.append(node.left)
            node_queue.append(node.right)
    return ','.join(res)

def deserialize(s):
    s = s.split(',')
    if s[0] == '#':
        return None
    root = TreeNode(int(s[0]))
    i = 0
    node_queue = [root]
    while node_queue:
        node = node_queue.pop(0)
        i += 1
        if s[i] != '#':
            node.left = TreeNode(int(s[i]))
            node_queue.append(node.left)
        i += 1
        if s[i] != '#':
            node.right = TreeNode(int(s[i]))
            node_queue.append(node.right)
    return root

def pre_order(root):
    res = []
    def sub(root):
        if not root:
            return
        res.append(root.val)
        sub(root.left)
        sub(root.right)
    sub(root)
    return res

def in_order(root):
    res = []
    def sub(root):
        if not root:
            return
        sub(root.left)
        res.append(root.val)
        sub(root.right)
    sub(root)
    return res

def post_order(root):
    res = []
    def sub(root):
        if not root:
            return
        sub(root.left)
        sub(root.right)
        res.append(root.val)
    sub(root)
    return res

def post_order0(root):
    res = []
    def sub(node):
        if not node:
            return
        res.append(node.val)
        sub(node.right)
        sub(node.left)
    sub(root)
    return res[::-1]    #reverse in order when right node first

def pre_order2(root):
    res = []
    node = root
    node_stack = []
    while node or node_stack:
        while node:
            res.append(node.val)    #get value when push
            node_stack.append(node)
            node = node.left
        node = node_stack.pop()
        node = node.right
    return res

def in_order2(root):
    res = []
    node = root
    node_stack = []
    while node or node_stack:
        while node:
            node_stack.append(node)
            node = node.left
        node = node_stack.pop()
        res.append(node.val)    #get value when pop
        node = node.right
    return res

def post_order2(root):
    res = []
    node = root
    node_stack = []
    while node or node_stack:
        while node:
            res.append(node.val)
            node_stack.append(node)
            node = node.right
        node = node_stack.pop()
        node = node.left
    return res[::-1]    #reverse in order when right node first

def get_tree_depth(root):
    if not root:
        return 0
    left = get_tree_depth(root.left)
    right = get_tree_depth(root.right)
    return max(left, right)+1

def is_balanced(root):
    if not root:
        return True
    left = get_tree_depth(root.left)
    right = get_tree_depth(root.right)
    if abs(left-right) > 1:
        return False
    res = is_balanced(root.left) and is_balanced(root.right)
    return res