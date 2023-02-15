import os
output_file = open(r"Directory_tree_structure.txt","a",encoding="utf8")

class BST:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        

    def insert_data(self,data,index):
        if self.data:
            if self.left == None:
                self.left = BST(data)
            elif self.right == None:
                self.right = BST(data)
            elif (self.left != None) and (index%2 != 0):
                self.left.insert_data(data,index)
            elif (self.right != None) and (index%2 == 0):
                self.right.insert_data(data,index)
        else:
            self.data = data
            return

    def bst_extract(self):
            if self == None:
                return
            if self.left:
                self.left.bst_extract()
            output_file.write(str(self.data))
            output_file.write("\n")
            if self.right:
                self.right.bst_extract()

directories_in_os = []

for (root,dirs,files) in os.walk('.',topdown=True):
    directories_in_os.append({"Root":root,"Dirs":dirs,"Files":files})
    break

node = []
node_counter = 0
node.append("Data to be entered")
node[node_counter] = BST(directories_in_os[0])
index = 1
counter = 1

"""
Applying BST to the data from os.walk()

"""

for (root,dirs,files) in os.walk('.',topdown=True):
    if counter%996 == 0:
        node.append("Data to be entered")
        node_counter = node_counter + 1
        node[node_counter] = BST({"File_Count":counter,"Root":root,"Dirs":dirs,"Files":files})
        index = 1
        counter = counter + 1
    else:
        node[node_counter].insert_data({"File_Count":counter,"Root":root,"Dirs":dirs,"Files":files},index)
        index = index + 1
        counter = counter + 1

for node_index in range(0,node_counter):
    node[node_index].bst_extract()


