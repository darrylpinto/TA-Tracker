__author__ = "Darryl Pinto"

"""
This is a program that helps TA decide which confused student to help when the
TA is ready to help
"""

import doublyLinkedList as dll
import heap as hp

class Student:
    """
    A Student consists of:
    :slot name: Name of the student (String)
    :slot confusion: The level of confusion (int)
    :slot previous: The previous student in the queue (Student)
    :slot next: The next student in the queue (Student)
    :slot position: The position of Student object in heap_array (int)
    """

    __slots__ = "name", "confusion", \
                "previous", "next", \
                "position"

    def __init__(self, name, confusion_level):
        """
        The constructor of Student
        :param name: Student name (string)
        :param confusion_level: The confusion level (int)
        """
        self.name = name
        self.confusion = confusion_level
        self.next = None
        self.previous = None
        self.position = None



def read_input(file):
    """
    Method to read the Input File and process the contents

    Each line of the File having student data should be in the following format:
    name_of_student confusion_level

    Each line of the File having TA data should be in the following format:
    name_of_TA ready

    NOTE: The program will exit with code -1 if the file is not found
          The program will exit with code 1 if confusion_level is not an integer
          The program will exit with code 2 if the line doesn't specify exactly
          2 arguments(including for Blank Lines)


    :param file: The name of input file (String)
    :return: file_data: List having the data from the file
    """

    try:
        fh = open(file)
    except IOError:
        print(str(file) + " Not Found!")
        exit(-1)

    file_data = fh.readlines()
    fh.close()

    for index in range(len(file_data)):
        file_data[index] = file_data[index].strip()

        if not (file_data[index] == "Oliver ready"
                or file_data[index] == "Colleen ready"):
            file_data[index] = file_data[index].split(" ")

    return file_data


def ta_tracker(file_data):
    """
    The method that tracks TA and specifies which confused student to help
    when the TA is ready to help
    :param file_data: List having the data from the file
    :return: None
    """
    oliver = dll.DoublyLinkedList()
    colleen = hp.Heap()

    for line in file_data:

        if not (line == "Oliver ready" or line == "Colleen ready"):

            if len(line) == 2:
                name = line[0]

                try:
                    confusion = int(line[1])
                except ValueError:
                    print("Incorrect Numerical Input!\nExiting")
                    exit(1)

                student = Student(name, confusion)
                oliver.insert(student)
                colleen.insert(student)
                print(student.name + " is looking for help!")
            else:
                print("Incorrect Input File! Encountered: " + str(line) +
                      "\nExiting")
                exit(2)

        else:
            if line == "Oliver ready":

                if not oliver.isEmpty():

                    student_helped = oliver.remove()
                    print("Oliver helping " + student_helped.name)
                    colleen.remove_middle(student_helped.position)

                else:

                    print("Oliver ready but he has no students to help")

            elif line == "Colleen ready":

                if not colleen.isEmpty():

                    student_helped = colleen.remove()
                    print("Colleen helping " + student_helped.name)
                    oliver.remove_middle(student_helped)

                else:

                    print("Colleen ready but she has no students to help")

    print("\nStudents left unhelped:")
    if not (oliver.isEmpty() and colleen.isEmpty()):
        print(oliver)
    else:
        print("-")

def main():
    """
    The main method
    :return: None
    """
    file = input("Enter the name of the file: ") + ".txt"
    file_data = read_input(file)
    ta_tracker(file_data)


if __name__ == "__main__":
    main()
