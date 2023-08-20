class TextEditor:
    def __init__(self):
        self.text = ""
        self.operations = []

    def append(self, W):
        self.operations.append(self.text)
        self.text += W

    def delete(self, k):
        self.operations.append(self.text)
        self.text = self.text[:-k]

    def print_char(self, k):
        return self.text[k - 1]

    def undo(self):
        if self.operations:
            self.text = self.operations.pop()


if __name__ == "__main__":
    editor = TextEditor()

    Q = int(input("Enter number of operations: "))
    for _ in range(Q):
        operation = input("Enter operation: ").split()
        op_type = int(operation[0])

        if op_type == 1:
            W = operation[1]
            editor.append(W)
        elif op_type == 2:
            k = int(operation[1])
            editor.delete(k)
        elif op_type == 3:
            k = int(operation[1])
            char = editor.print_char(k)
            print(char)
        elif op_type == 4:
            editor.undo()
