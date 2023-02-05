def getTreeTraversal(root):
    # Write your code here.
    pro = []
    io = []
    poo = []

    stack = [(root,1)]
    # 1 -> pre 
    # 2 -> io
    # 3 -> post

    while stack:
        curr, code = stack.pop()

        if curr is None : 
            continue
        
        if code == 1 :
            pro.append(curr.data)
            stack.append((curr, 2))
            stack.append((curr.left, 1))
        
        elif code == 2 :
            io.append(curr.data)
            stack.append((curr, 3))
            stack.append((curr.right, 1))

        elif code == 3 : 
            poo.append(curr.data)




# https://www.youtube.com/watch?v=ySp2epYvgTE