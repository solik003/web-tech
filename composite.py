# Component interface
class FileSystemComponent:
    def __init__(self, name):
        self.name = name

    # Common method to display the name of the component
    def display(self):
        raise NotImplementedError("Method 'display' must be implemented")


# Composite class representing directories
class Directory(FileSystemComponent):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    # Add a child component to the directory
    def add(self, component):
        self.children.append(component)

    # Display the name of the directory and its contents recursively
    def display(self):
        print(f"Directory: {self.name}")
        for child in self.children:
            child.display()


# Leaf class representing files
class File(FileSystemComponent):
    def __init__(self, name):
        super().__init__(name)

    # Display the name of the file
    def display(self):
        print(f"File: {self.name}")


# Usage
root = Directory("Root")

folder1 = Directory("Folder 1")
folder1.add(File("File 1.1"))
folder1.add(File("File 1.2"))

folder2 = Directory("Folder 2")
folder2.add(File("File 2.1"))

root.add(folder1)
root.add(folder2)

root.display()
