import sys


class Stack:

    def __init__(self):
        # Для хранения элементов в списке используем приватный атрибут.
        # На его приватность указывают два подчёркивания в имени.
        self.__items = []

    def push(self, item):
        """Добавить элемент в стек."""
        self.__items.append(item)

    def pop(self):
        """Взять элемент из стека."""
        return self.__items.pop()

    def peek(self):
        """Посмотреть последний элемент без изъятия."""
        return self.__items[-1]

    def size(self):
        """Вернуть размер стека."""
        return len(self.__items)


def characters_is_valid(characters_list, characters_stack):
    for item in characters_list:
        if '(' == item or '[' == item or '{' == item:
            characters_stack.push(item)
        if characters_stack.size() == 0:
            return False
        if item == ')':
            if characters_stack.peek() == '(':
                characters_stack.pop()
            else:
                return False
        if item == ']':
            if characters_stack.peek() == '[':
                characters_stack.pop()
            else:
                return False
        if item == '}':
            if characters_stack.peek() == '{':
                characters_stack.pop()
            else:
                return False

    if characters_stack.size() == 0:
        return True
    else:
        return False


def main():
    characters_list = sys.stdin.readline().rstrip()
    characters_list = list(characters_list)
    characters_stack = Stack()
    brackets_is_valid = characters_is_valid(characters_list, characters_stack)

    if brackets_is_valid:
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    main()
