class TreeObj:
    def __init__(self, index: int, value: str=None) -> None:
        self.index = index
        self.value = value
        self.left = self.right = None

    @property
    def left(self):
        return self.__left
    
    @left.setter
    def left(self, obj):
        self.__left = obj

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, obj):
        self.__right = obj

class DecisionTree:
    #questions = ["Loves python?", "Understand OOP?", "Loves \"Panda Kung-Fu\"?"]

    @classmethod
    def predict(cls, root: TreeObj, x):
        obj = root
        while not obj.value:
            obj = obj.left if x[obj.index] else obj.right
        return obj.value

    @classmethod
    def add_obj(cls, obj: TreeObj, node: TreeObj=None, left: bool=True) -> TreeObj:
        if node:
            if left:
                node.left = obj
            else:
                node.right = obj
        return obj

root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "Will be programmer"), v_11)
DecisionTree.add_obj(TreeObj(-1, "Will be codder"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "Not all lost"), v_12)
DecisionTree.add_obj(TreeObj(-1, "Lost"), v_12, False)

x = [0, 0, 0]

res = DecisionTree.predict(root, x)
print(res)