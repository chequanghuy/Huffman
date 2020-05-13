class Node(object):
    def __init__(self, parent=None, left=None, right=None, weight=0, symbol=''):
        super(Node, self).__init__()
        self._parent = parent
        self._left = left
        self._right = right
        self._weight = weight
        self._symbol = symbol

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, left):
        self._left = left

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right):
        self._right = right

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        self._symbol = symbol

    #lấy chuỗi từ node đến nút lá có symbol là "s"
    def get_code(self, s, node, code=""):
        if node.left is None and node.right is None:    #nếu node không có node lá
            return code if node.symbol == s else ''     #return chuỗi dẫn đến ký tự s, nếu đi đến node lá cuối vẫn không tìm được ký tự thì đường đi đã sai
        else:
            temp = ""                                   
            if node.left is not None:
                temp = self.get_code(s, node.left, code+"0")
            if not temp and node.right is not None:     #nếu đã tìm được chuỗi thì kh thực hiện lệnh if này
                temp = self.get_code(s, node.right, code+"1")
            return temp                                 #return chuỗi dẫn đến ký tự s
