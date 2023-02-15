
# File details extract

Extract all the file information available in the system

# Algorithm

- Creating a class BST
- Insert operation of BST
- BST data extraction

- OS.walk() generate the file names in a directory tree by walking the tree either top-down or bottom-up.   For each directory in the tree rooted at directory top (including top itself), it yields a 3-tuple (dirpath, dirnames, filenames).

    root : Prints out directories only from what you specified.
    dirs : Prints out sub-directories from root.
    files : Prints out all files from root and directories.


- for (root,dirs,files) in os.walk('.',topdown=True):

        node[node_counter].insert_data({"File_Count":counter,"Root":root,"Dirs":dirs,"Files":files},index)

        index = index + 1

        counter = counter + 1



