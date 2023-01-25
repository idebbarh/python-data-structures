class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = [self.data]

        if self.left:
            elements+=self.left.pre_order_traversal()

        if self.right:
            elements+=self.right.pre_order_traversal()

        return elements

    def find_min(self):
        if self.left :
            return self.left.find_min()
        else :
            return self.data

    def find_max(self):
        if self.right :
            return self.right.find_max()
        else :
            return self.data

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

    def remove(self,data):
        if data < self.data :
            if self.left :
                self.left = self.left.remove(data)

        if data > self.data :
            if self.right :
                self.right = self.right.remove(data)

        else :
            if self.left is None :
                return self.right 

            if self.right is None :
                return self.left

            smallest = self.right.find_min()
            self.data = smallest
            self.right = self.right.remove(smallest)

        return self

            


def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers_tree = build_tree([17, 4, 20, 9, 23, 18, 34, 100])
    numbers_tree.calculate_sum()
    numbers_tree.remove(23)
    print(numbers_tree.in_order_traversal())