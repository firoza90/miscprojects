class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self, values):
        """ Create binary tree from list representing level order traversal """
        nodes = [None if value == None else TreeNode(value) for value in values]
        child = nodes[::-1]
        self.root = child.pop()
        for node in nodes:
            if node:
                if child:
                    node.left = child.pop()
                if child:
                    node.right = child.pop()

    def __repr__(self) -> str:
        """ gives level order traversal of tree """
        pass

    def drawTree(self):
        oneLevelHeight = 60
        def jumpTo(x, y):
            t.penup()
            t.goto(x, y)
            t.pendown()

        def drawNode(root, x, y, gap):
            if not root:
                return
            t.goto(x, y)
            jumpTo(x, y-20)
            t.write(root.val, align='center', font=('Arial', 12, 'normal'))
            t.circle(10)
            drawNode(root.left, x-gap, y-oneLevelHeight, gap/2)
            jumpTo(x, y-20)
            drawNode(root.right, x+gap, y-oneLevelHeight, gap/2)

        def height(root):
            return 1 + max(height(root.left), height(root.right)) if root else -1

        import turtle
        t = turtle.Turtle()
        t.speed(0); turtle.delay(0)
        h = height(self.root)
        gap = h*40
        drawNode(self.root, 0, 0, gap)
        t.hideturtle()
        turtle.mainloop()




