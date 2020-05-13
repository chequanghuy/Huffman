from node import Node
class static_Huffman:
    def __init__(self):
        
        self.only_letters=[] #chỉ lưu các ký tự xuất hiện
        self.Nodes=[]        #lưu ký tự và tần số suất hiện
        self.Tree=[]         #

    def take_fre(self,elem):    #sắp xếp theo trọng số
        return elem._weight

    def take_c(self,elem):  #sắp xếp theo ký tự
        return elem._symbol

    def combine(self,Nodes): #xây dựng huffman_tree
        pos=0
        newnode=Node(symbol="",weight=0)  
        self.Nodes.sort(key=self.take_c,reverse=False)
        self.Nodes.sort(key=self.take_fre,reverse=False)
        if len(self.Nodes)>1:            
            combined_node1=(self.Nodes[pos]._symbol+self.Nodes[pos+1]._symbol)      #tổng trọng số của hai nút lá
            combined_node2=(self.Nodes[pos]._weight+self.Nodes[pos+1]._weight)      #ghép ký tự của hai nút lá           
            #new node sẽ là node gốc của hai node lá chứa trọng số và ký tự đã ghép của hai node lá
            newnode=Node(symbol=combined_node1,weight=combined_node2,left=self.Nodes[pos],right=self.Nodes[pos+1])
            self.Nodes=self.Nodes[2:] 
            self.Nodes.append(newnode)                             
            self.Tree.append(newnode)
            self.combine(Nodes)                      #jump đến hàm combine


    def Solve_nodes(self,my_string):    #tạo list nodes chứa các node
        letters=[]       
        for letter in my_string:    #lấy từng ký tự trong string để kiểm tra
            if letter not in self.only_letters:   #nếu ký tự chưa xuất hiện trong only_letter
                freq=my_string.count(letter)    #đếm tần suất xuất hiện của ký tự đó
                letters.append(freq)        #thêm tần suất
                letters.append(letter)      #thêm ký tự
                self.only_letters.append(letter)     #...       
        while len(letters)>0:
            node=Node(weight=0,symbol=0)
            node._symbol=letters[1]
            node._weight=letters[0]
            self.Nodes.append(node)
            # nodes.append(letters[0:2])  #lấy 2 phần tử đầu tiên 
            letters=letters[2:]     #loại bỏ hai phần tử đầu tiên

    def create_Tree(self):          #tạo cây từ nodes
        for i in self.Nodes:
            self.Tree.append(i)
        self.combine(self.Nodes)        
        self.Tree.sort(key=self.take_c,reverse=True)
        self.Tree.sort(key=self.take_fre,reverse=True)

    def Binary_Table(self,my_string):   #tạo bảng ký tự binary từ cây huffman
        letter_binary=[]       
        if len(self.only_letters)==1:
            letter_code=[self.only_letters[0],"0"]   
            letter_binary.append(letter_code*len(my_string))            
        else:
            root=self.Tree[0]
            for letter in self.only_letters:
                lettercode=""
                lettercode=Node().get_code(letter,root)        
                letter_code=[letter,lettercode]
                letter_binary.append(letter_code)
        print("binary code:")
        for letter in letter_binary:
            print(letter[0],letter[1])
        return letter_binary
    def encode(self,my_string):     #nén chuỗi   
        letter_binary=[]
        self.Solve_nodes(my_string)
        self.create_Tree()        
        letter_binary=self.Binary_Table(my_string)
        bitstring=""
        for character in my_string:
            for item in letter_binary:
                if character in item:
                    bitstring=bitstring+item[1]
        return bitstring
       
file = open("test.txt", "r")    #mở file
str_t= file.read()              #đọc file
str_t=str(str_t)                
result = static_Huffman().encode(str_t)     #nén và lưu trong result
file.close()                    #đóng file
print(result)                   #in kết quả ra terminal
