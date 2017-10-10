
class Heap:
    """
    The heap consists of:
    :slot heap_array: The list of Student objects  (list)
    :slot heap_size: Current Heap Size (int)
    """

    __slots__ = ('heap_array', 'heap_size')

    def __init__(self):
        """
        The constructor of Heap
        """

        self.heap_array = []
        self.heap_size = 0

    def isEmpty(self):
        """
        Method to check is heap is empty or not
        :return: Boolean indicating is heap is empty or not
        """
        return self.heap_size == 0

    def __leftChild(self, location):
        """
        Helper Method to return the left child of student at position specified by
        location in heap_array
        :param location: The position of student (int)
        :return:  position of the left child (int)
        """
        return 2 * location + 1

    def __rightChild(self, location):
        """
        Helper Method to return the right child of student at position specified by
        location in heap_array
        :param location: The position of student (int)
        :return:  position of the right child (int)
        """
        return 2 * location + 2

    def __parent(self, location):
        """
        Helper Method to return the parent of student at position specified by
        location in heap_array
        :param location: The position of student (int)
        :return:  position of the left child (int)
        """
        return (location - 1) // 2

    def __swap(self, location1, location2):
        """
        Helper Method to swap node at location1 with node at location2
        :param location1: first node's position (int)
        :param location2: second node's position (int)
        :return: None
        """

        self.heap_array[location1], self.heap_array[location2] = \
            self.heap_array[location2], self.heap_array[location1]

        self.heap_array[location1].position, \
            self.heap_array[location2].position = \
            self.heap_array[location2].position, \
            self.heap_array[location1].position

    def __bubbleUp(self, location):
        """
        Helper Method that handles the swapping of a node with its parent
        :param location: position of the node (int)
        :return: None
        """
        while location > 0 and \
                        self.heap_array[location].confusion > \
                        self.heap_array[self.__parent(location)].confusion:
            self.__swap(location, self.__parent(location))
            location = self.__parent(location)

    def __bubbleDown(self, location):
        """
        Helper Method that handles the swapping of a node with its children
        :param location: position of the node (int)
        :return: None
        """
        new_location = self.__greatest(location)
        while new_location != location:
            self.__swap(location, new_location)
            location = new_location
            new_location = self.__greatest(location)

    def __greatest(self, location):
        """
        Helper method that returns the position of the greatest node among a
        node and its children
        :param location: position of the node (int)
        :return: the position of the greatest node (int)
        """
        left_child = self.__leftChild(location)
        right_child = self.__rightChild(location)

        if left_child >= self.heap_size:
            return location

        if right_child >= self.heap_size:
            if self.heap_array[location].confusion > \
                    self.heap_array[left_child].confusion:

                return location
            else:
                return left_child

        if self.heap_array[left_child].confusion > \
                self.heap_array[right_child].confusion:

            if self.heap_array[location].confusion > \
                    self.heap_array[left_child].confusion:
                return location
            else:
                return left_child
        else:
            if self.heap_array[location].confusion > \
                    self.heap_array[right_child].confusion:
                return location
            else:
                return right_child

    def insert(self, node):
        """
        Method to insert node in the heap
        :param node: node to be inserted (Student)
        :return: None
        """
        if self.heap_size < len(self.heap_array):
            self.heap_array[self.heap_size] = node
        else:
            self.heap_array.append(node)
        node.position = self.heap_size
        self.__bubbleUp(self.heap_size)

        self.heap_size += 1

    def remove(self):
        """
        Method to remove the node with most priority
        :return: the node with most priority (Student)
        """
        top_heap = self.heap_array[0]
        self.heap_size -= 1
        if self.heap_size > 0:
            self.heap_array[0] = self.heap_array[self.heap_size]
            self.heap_array[0].position = 0
            self.__bubbleDown(0)

        return top_heap

    def remove_middle(self, location):
        """
        Method to remove the node from middle of the heap
        :param location: position of node to be removed (int)
        :return: None
        """
        self.heap_size -= 1

        self.heap_array[self.heap_size].position = \
            self.heap_array[location].position

        self.heap_array[location] = self.heap_array[self.heap_size]

        if self.heap_array[location].confusion > \
                self.heap_array[self.__parent(location)].confusion:
            self.__bubbleUp(location)
        else:
            self.__bubbleDown(location)

    def __str__(self):
        """
        Method to return String representation of the heap
        :return: String representation of the heap (String)
        """
        string = ""
        for s in range(self.heap_size):
            string += str(self.heap_array[s].name) \
                      + "," + str(self.heap_array[s].confusion) + " "

        return string

