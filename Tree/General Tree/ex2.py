class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self,lv):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        if self.get_level() <= lv:
            print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(lv)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_product_tree():
    root = TreeNode("Global")

    india = TreeNode("India")
    gujarat = TreeNode("Gujarat")
    gujarat.add_child(TreeNode("Ahmedabad"))
    gujarat.add_child(TreeNode("Baroda"))
    karnataka = TreeNode("Karnataka")
    karnataka.add_child(TreeNode("Bangluru"))
    karnataka.add_child(TreeNode("Mysore"))
    india.add_child(gujarat)
    india.add_child(gujarat)

    usa = TreeNode("Usa")
    new_jersey = TreeNode("New Jersey")
    new_jersey.add_child(TreeNode("Princeton"))
    new_jersey.add_child(TreeNode("Trenton"))
    califonia = TreeNode("Califonia")
    califonia.add_child(TreeNode("San Francisco"))
    califonia.add_child(TreeNode("Mountain View"))
    califonia.add_child(TreeNode("Palo Alto"))
    usa.add_child(new_jersey)
    usa.add_child(califonia)

    root.add_child(india)
    root.add_child(usa)

    root.print_tree(1)
    root.print_tree(2)
    root.print_tree(3)

if __name__ == '__main__':
    build_product_tree()