
from node import Node

class adaptive_Huffman():
    def __init__(self):        
        self.NYT = Node(symbol="NYT")
        self.root = self.NYT                #root mặc định là cây NYT
        self.nodes = []                     #lưu các node với vị trí các node trong mảng cũng là số thứ tự của các node
        self.seen = [None] * 256            #tối đa 256 ký tự

    def find_largest_node(self, weight):    #tìm node có trọng số cao nhất = weight
        for n in reversed(self.nodes):      #duyệt chuỗi từ 
            if n.weight == weight:          #
                return n

    def swap_node(self, n1, n2):
        #đổi chỗ hai node
        i1, i2 = self.nodes.index(n1), self.nodes.index(n2)
        self.nodes[i1], self.nodes[i2] = self.nodes[i2], self.nodes[i1]
        tmp_parent = n1.parent
        n1.parent = n2.parent
        n2.parent = tmp_parent
        #TH đặc biệt: hai node có liên kết với nhau 
        if n1.parent.left is n2:
            n1.parent.left = n1
        elif n1.parent.right is n2:
            n1.parent.right = n1
        if n2.parent.left is n1:
            n2.parent.left = n2
        elif n2.parent.right is n1:
            n2.parent.right = n2

    def insert(self, s):
        node = self.seen[ord(s)]    #nếu ký tự s chưa xuất hiện thì node is None
        if node is None:                        #ký tự s chưa xuất hiện
            spawn = Node(symbol=s, weight=1)    #tạo node mới có symbol là s
            internal = Node(symbol='', weight=1, parent=self.NYT.parent,    #tạo nút mới là nút cha của NYT và spawn
                left=self.NYT, right=spawn)
            spawn.parent = internal
            self.NYT.parent = internal
            if internal.parent is not None:     #nếu đã có root
                internal.parent.left = internal 
            else:                               #nếu chưa có root
                self.root = internal              
        #Chèn nút mới (Ký tự | trọng số = 1) vào NYT. Đánh lại số thứ tự.
            self.nodes.insert(0, internal)           
            self.nodes.insert(0, spawn)
            self.seen[ord(s)] = spawn           #lưu lại ký tự 
            node = internal.parent              
        while node is not None:                 #điều chỉnh lại cây
            #tìm node có trọng số lớn nhất và bằng trọng số của node
            largest = self.find_largest_node(node.weight)
            #nếu node không phải largest và node không phải largest.parent và largest không phải node.parent
            #tính chất anh em
            if (node is not largest and node is not largest.parent and
                largest is not node.parent):
                self.swap_node(node, largest)
            node.weight = node.weight + 1       #tăng trọng số của node
            node = node.parent                  #tăng trọng số của các node cha
    def encode(self, text):
        result = ''     #chuỗi kết quả
        for s in text:  #duyệt từng ký tự trong text
            if self.seen[ord(s)]:   #nếu ký tự đã tồn tại
                result += Node().get_code(s, self.root)       #đường dẫn đến ký tự "s"
            else:                   #nếu ký tự chưa tồn tại
                result += Node().get_code('NYT', self.root)   #đường dẫn đến NYT
                result += bin(ord(s))[2:].zfill(8)         #chuyển sang mã bit của ký tự (8 ký tự)
            self.insert(s)                                  #chèn nút dô cây và chỉnh lại cây
        return result

 

file = open("test.txt", "r")
str_t= file.read()
str_t=str(str_t)
result = adaptive_Huffman().encode(str_t)
file.close()
print(result)

