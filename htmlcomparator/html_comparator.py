from html.parser import HTMLParser


class Node:
    def __init__(self, tag, attrs):
        self.tag = tag
        self.attrs = {}
        for p in attrs:
            self.attrs[p[0]] = p[1]
        self.data = None
        self.children = []

        self.pos = None

    def add_data(self, data):
        self.data = data

class HTMLTree:
    def __init__(self, root = None):
        self.root = root 
        self.decl = None
    
    
class ParseToTree(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tree = None
        self.stack = []

    def handle_starttag(self, tag, attrs):
        n = Node(tag, attrs)
        if not self.tree:
            self.tree = HTMLTree(n)
        elif not self.tree.root:
            self.tree.root = n
        if self.stack:
            self.stack[-1].children.append(n)
        self.stack.append(n)

    def handle_endtag(self, tag):
        if not self.stack or self.stack[-1].tag != tag:
            raise ParsingError("Malformed HTML file")
        self.stack.pop()

    def handle_data(self, data):
        self.stack[-1].add_data(data)

    def handle_decl(decl):
        if not self.tree:
            self.tree = HTMLTree()
            self.tree.decl = decl
        else:
            self.tree.decl = decl


class HTMLComparator:
    def __init__(self):
        pass

    def compare_files(self, o1, o2):
        if type(o1) == str and type(o2) == str:
            c1 = o1
            c2 = o2 
        elif type(o1) == file and type(o2) == file:
            c1 = o1.read()
            c2 = o2.read()
        else:
            raise TypeError("arguments are not file objects or strings")

        parse1 = ParseToTree()
        parse1.feed(c1)

        parse2 = ParseToTree()
        parse2.feed(c2)

        return self._compare_trees(parse1, parse2)

    def _compare_trees(self, t1, t2):
        if t1.tree.decl != t2.tree.decl:
            print("doctype declarations different")
            return False
        queue1 = [t1.tree.root]
        queue2 = [t2.tree.root]
        while queue1 and queue2:
            node1 = queue1.pop(0)
            node2 = queue2.pop(0)
            if node1.tag != node2.tag:
                print(node1.tag + " is different from " + node2.tag)
                return False
            if node1.attrs != node2.attrs:
                print("attributes of " + node1.tag + " and " + node2.tag + " are different")
                return False
            if node1.data != node2.data:
                print("data of " + node1.tag + " and " + node2.tag + " are differnet")
                return False
            if len(node1.children) != len(node2.children):
                print(" different number of childrens")
                return False
            queue1 += node1.children
            queue2 += node2.children
        return True
            
            
class ParsingError(Exception):
    pass
