class TreeNode:
    def __init__(self,data_name,data_pos) :
        self.data_name = data_name
        self.data_pos = data_pos
        self.children = []
        self.parent = None
    
    def get_level(self):

        level = 0
        p = self.parent

        while p:
            level+=1
            p = p.parent

        return level

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def print_tree_data(self,part):
        space = " "* self.get_level()*3
        prefix = space+"|__" if self.parent else ""

        if part == "name":
            print(prefix+self.data_name)

        elif part == "designation" :
            print(prefix+self.data_pos)

        else :
            print(f"{prefix}{self.data_name} ({self.data_pos})")

        if self.children :
            for child in self.children :
                child.print_tree_data(part)

def creat_tree_node():
    root = TreeNode("Nilupul","CEO")

    chinmay = TreeNode("Chinmay","CTO")
    vishwa = TreeNode("Vishwa","Infrastructure Head")
    vishwa.add_child(TreeNode("Dhaval","Cloud Manager"))
    vishwa.add_child(TreeNode("abhijit","App Manager"))
    chinmay.add_child(vishwa)
    chinmay.add_child(TreeNode("Amir","Application Head"))

    gels = TreeNode("Gels","HR Head")
    gels.add_child(TreeNode("Peter","Recruitment Manager"))
    gels.add_child(TreeNode("Waqas","Policy Manager"))
    root.add_child(chinmay)
    root.add_child(gels)

    root.print_tree_data("name")
    print("#"*50)
    root.print_tree_data("designation")
    print("#"*50)
    root.print_tree_data("both")
creat_tree_node()