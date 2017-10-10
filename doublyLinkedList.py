class DoublyLinkedList:
    """
    The Doubly Linked List consists of:
    :slot head: The reference of the first node in the list (Student)
    :slot tail: The reference of the last node in the list (Student)
    """
    __slots__ = "head", "tail"

    def __init__(self):
        """
        The constructor of DoublyLinkedList
        """
        self.head = None
        self.tail = None

    def isEmpty(self):
        """
        Method to check if DoublyLinkedList is empty
        :return: boolean indicating if the DoublyLinkedList is empty or not
        """

        return self.head is None

    def insert(self, node):
        """
        Method to insert node in the DoublyLinkedList
        :param node: node to be inserted (Student)
        :return: None
        """
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            node.previous = self.tail

        self.tail = node

    def remove(self):
        """
        Method to remove first node in the DoublyLinkedList
        :return: node to be removed (Student)
        """
        if self.head.next is None:

            student = self.head
            self.head = self.tail = None
            return student

        else:

            student = self.head
            self.head = self.head.next
            self.head.previous = None
            return student

    def remove_middle(self, node):
        """
        Method to remove the node from middle of the DoublyLinkedList
        :param node: node to be removed (Student)
        :return: None
        """
        if node.previous is None and node.next is None:
            self.head = self.tail = None

        elif node.next is None:

            node.previous.next = None
            self.tail = self.tail.previous

        elif node.previous is None:
            node.next.previous = None
            self.head = self.head.next

        else:

            node.next.previous = node.previous
            node.previous.next = node.next

    def __str__(self):
        """
        Method to return String representation of the DoublyLinkedList
        :return: String representation of the DoublyLinkedList (String)
        """
        string = ""
        traversal_node = self.head

        while traversal_node is not None:
            string += str(traversal_node.name) + "\n"

            traversal_node = traversal_node.next

        return string

