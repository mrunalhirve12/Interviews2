"""
Design an in-memory file system to simulate the following functions:

ls: Given a path in string format. If it is a file path, return a list that only contains this file's name. If it is a directory path, return the list of file and directory names in this directory. Your output (file and directory names together) should in lexicographic order.

mkdir: Given a directory path that does not exist, you should make a new directory according to the path. If the middle directories in the path don't exist either, you should create them as well. This function has void return type.

addContentToFile: Given a file path and file content in string format. If the file doesn't exist, you need to create that file containing given content. If the file already exists, you need to append given content to original content. This function has void return type.

readContentFromFile: Given a file path, return its content in string format.



Example:

Input:
["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
[[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]

Output:
[null,[],null,null,["a"],"hello"]

Explanation:
filesystem


Note:

You can assume all file or directory paths are absolute paths which begin with / and do not end with / except that the path is just "/".
You can assume that all operations will be passed valid parameters and users will not attempt to retrieve file content or list a directory or file that does not exist.
You can assume that all directory names and file names only contain lower-case letters, and same names won't exist in the same directory.
"""
import collections

"""We'll keep two structures, self.fs being a Trie, and self.fileinfo being a dictionary mapping filepaths to the string content in their files. For convenience, we can use a nested defaultdict structure instead of a proper Trie object. This means we should exercise caution as our call to TrieNode.__getitem__(child)
 has potential side effects if child is not in the node, but otherwise our code is very similar."""
Trie = lambda: collections.defaultdict(Trie)

class FileSystem(object):
    def __init__(self):
        self.fs = Trie()
        self.fileinfo = collections.defaultdict(str)

    def ls(self, path):
        if path in self.fileinfo:
            return path.split('/')[-1:]

        cur = self.fs
        for token in path.split('/'):
            if token in cur:
                cur = cur[token]
            elif token:
                return []

        return sorted(cur.keys())

    def mkdir(self, path):
        cur = self.fs
        for token in path.split('/'):
            if token: cur = cur[token]

    def addContentToFile(self, filePath, content):
        self.mkdir(filePath)
        self.fileinfo[filePath] += content

    def readContentFromFile(self, filePath):
        return self.fileinfo[filePath]

"""Here is the same solution using a TrieNode object."""

class Node(object):
    def __init__(self):
        self.children = {}

    def setdefault(self, token):
        return self.children.setdefault(token, Node())

    def get(self, token):
        return self.children.get(token, None)

class FileSystem(object):
    def __init__(self):
        self.root = Node()
        self.fileinfo = collections.defaultdict(str)

    def ls(self, path):
        if path in self.fileinfo:
            return path.split('/')[-1:]

        cur = self.root
        for token in path.split('/'):
            if cur and token:
                cur = cur.get(token)

        return sorted(cur.children.keys()) if cur else []

    def mkdir(self, path):
        cur = self.root
        for token in path.split('/'):
            if token: cur = cur.setdefault(token)