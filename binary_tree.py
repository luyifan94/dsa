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

def is_tree_node(root, a):
    if root is None or a is None:
        return False
    if root is a:
        return True
    #left = is_tree_node(root.left, a)
    #right = is_tree_node(root.right, a)
    #return left or right
    res = is_tree_node(root.left, a) or is_tree_node(root.right, a)
    #此写法的优点在当第一选项为真时就能结束运算
    return res

def lca(root, a, b):
    #假设a和b均在root中，所以需要选判断is_tree_node
    if root is None or root is a or root is b:
        return root
        #存在问题，假如b在a的子节点，此函数搜寻到a就返回了，lca就是a
        #若a在root中，但是b不在root中，搜寻到a返回后，会得到a是lca，但实际b并不在root中，这个情况result就错误了
    left = lca(root.left, a, b)
    right = lca(root.right, a, b)

    if left and right:
        return root
        #若左右子树都不为空，此节点为最近公共祖先，返回此节点
    else:
        return left or right
        #若左右都为空则返回空，若有一子树不为空则返回，返回的可能是最近公共祖先或者是ab中的一个(或None)