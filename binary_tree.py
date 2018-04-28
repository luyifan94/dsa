class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def serialize(root):
    ch = []
    node_queue = [root]
    while node_queue:
        node = nodeq.pop(0)
        if node == None:
            ch.append('#')
        else:
            ch.append(str(node.val) + ',')
            node_queue.append(node.left)
            node_queue.append(node.right)
    return ''.join(ch)

def deserialize(s):
    s1 = s.split(',')
    if s1[0] == '#':
        return None
    root = TreeNode(int(s1[0]))
    node_queue = [root]
    i = 0
    while node_queue:
        node = node_queue.pop(0)
        i += 1
        if s1[i] != '#':
            left = TreeNode(int(s1[i]))
            node.left = left
            node_queue.append(left)
        i += 1
        if s1[i] != '#':
            right = TreeNode(int(s1[i]))
            node.right = right
            node_queue.append(right)
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
    if not root:
        return
    res = []
    node_stack = []
    node = root
    while node or node_stack:
        while node:
            res.append(node.val)    #get value when push
            node_stack.append(node)
            node = node.left
        node = node_stack.pop()
        node = node.right
    return res

def in_order2(root):
    if not root:
        return
    res = []
    node_stack = []
    node = root
    while node or node_stack:
        while node:
            node_stack.append(node)
            node = node.left
        node = node_stack.pop()
        res.append(node.val)    #get value when pop
        node = node.right
    return res

def post_order2(root):
    if not root:
        return
    res = []
    node_stack = []
    node = root
    while node or node_stack:
        while node:
            res.append(node.val)
            node_stack.append(node)
            node = node.right
        node = node_stack.pop()
        node = node.left
    return res[::-1]    #reverse in order when right node first