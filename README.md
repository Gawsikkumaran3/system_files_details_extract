
# File details extract

Extract all the file information available in the system

# Algorithm

- Creating a class BST
- Insert operation of BST
- BST data extraction

- for (root,dirs,files) in os.walk('.',topdown=True):

        node[node_counter].insert_data({"File_Count":counter,"Root":root,"Dirs":dirs,"Files":files},index)

        index = index + 1

        counter = counter + 1



