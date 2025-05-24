def get_todos(filepath="todos.txt"):
    """
    Reads the text file and return the
    List of to-do items
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """ Write the to-do items list into text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)