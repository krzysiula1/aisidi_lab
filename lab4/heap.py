from abstract_heap import AbstractHeap

class Heap(AbstractHeap):
    def __init__(self, arny):
        self.values = []
        self.length = 0
        self.arny = arny
    
    def __str__(self):
        if self.length == 0:
            return 'Empty heap'
        if self.get_rows_number() < 4 and self.arny < 4 and self.max_three_digit():
            return self.get_string_complex()
        return self.get_string_simple()
    
    def __len__(self) -> int:
        return self.length

    def push(self, value):
        self.values.append(value)
        self.move_up(self.length)
        self.length+=1
        
    def move_up(self, index):
        
        if index == 0:
            return
        parent = self.parent(index)
        if self.values[index] > self.values[parent]:
            self.swap(index, parent)
            self.move_up(parent)

    def swap(self, index1, index2):
        (self.values[index1], self.values[index2]) = (self.values[index2], self.values[index1])
    
    def parent(self, i):
            return (i-1)//self.arny

    def children(self, index):
        return range(index*self.arny+1, index*self.arny+self.arny+1)

    def get_max_child(self, index):
        children = self.children(index)
        max = 0
        index_max = None
        for child in children:
            if child < self.length:
                if self.values[child] > max:
                    index_max = child
                    max = self.values[child]
        return index_max

    def get_rows_number(self):
        r = 0
        i = 0
        s = self.length
        while True:
            if s <= 0:
                return r
            s -= self.arny**i
            r+=1
            i+=1

    def get_rows(self):
        result = []
        rows = self.get_rows_number()
        start = 0
        end = 1
        for i in range(rows):
            if i == rows-1:
                result.append(self.values[start:])
            else:
                result.append(self.values[start:end])
            start += self.arny**i
            end += self.arny**(i+1)
        return result
    
    def get_string_simple(self):
        result = ''
        rows = self.get_rows_number()
        for i, row in enumerate(self.get_rows()):
            if i == rows-1:
                result += f'{i+1}' + '\n' + str(row) + '\n'
            else:
                result += f'{i+1}' + '\n' + str(row) + '\n'
        return result

    def get_string_complex(self):
        if self.arny == 2:
            return self.get_string_complex_2()
        elif self.arny == 3:
            return self.get_string_complex_3()
    
    def get_string_complex_2(self):
        result = ''
        rows = self.get_rows_number()
        width = 2**(rows-1)*5
        for i, row in enumerate(self.get_rows()):
                result += ' '*((width - 2**i*5)//2)
                for number in row:
                    if number < 10:
                        result += f'  {number}  '
                    elif number < 100:
                        result += f'  {number} '
                    elif number < 1000:
                        result += f' {number} '
                result += '\n'
                if i == 0 and rows > 1:
                    result += ' '*((width - 2**i*5)//2+1) + '/ \\'
                    result += '\n'
                    result += ' '*((width - 2**i*5)//2+1) + '|  \\'
                    result += '\n'
                    result += ' '*((width - 2**i*5)//2) + '/    |'
                elif i == 1 and rows > 2:
                    result += '      /|    |\\'
                    result += '\n'
                    result += '    -- |    | --'
                    result += '\n'
                    result += '   /   |    |   \\'
                result += '\n'
            
        return result

    def get_string_complex_3(self):
        result = ''
        rows = self.get_rows_number()
        width = 3**(rows-1)*5
        for i, row in enumerate(self.get_rows()):
                if i == 1 and rows > 2:
                    result += ' '*((width - 3**i*5)//2-7) + '-'*7
                else:
                    result += ' '*((width - 3**i*5)//2)
                for number in row:
                    if number < 10:
                        result += f'  {number}  '
                    elif number < 100:
                        result += f'  {number} '
                    elif number < 1000:
                        result += f' {number} '
                if i == 1 and rows > 2:
                   result += '-'*7
                result += '\n'
                if i == 0 and rows > 1:
                    result += ' '*((width - 3**i*5)//2+1) + '/|\\'
                    result += '\n'
                    result += ' '*((width - 3**i*5)//2-1) + '-- | --'
                    result += '\n'
                    result += ' '*((width - 3**i*5)//2-2) + '/   |   \\'
                elif i == 1 and rows > 2:
                    result += '       /        /|   /|\\   |\\        \\'
                    result += '\n'
                    result += '      /    ----/ /  / | \\  | \\----    \\'
                    result += '\n'
                    result += '     /    /     /   | | |   \\     \\    \\'
                    result += '\n'
                    result += '    /    /    --   /  |  \\   --    \\    \\'
                    result += '\n'
                    result += '   /    /    /    /   |   \\    \\    \\    \\'
                result += '\n'
            
        return result
    
    def max_three_digit(self):
        for i in self.values:
            if i >= 1000:
                return False
        return True
    
    def move_down(self, index):
        max_child = self.get_max_child(index)
        if max_child:
            if self.values[max_child] > self.values[index]:
                self.swap(index, max_child)
                self.move_down(max_child)

    def peek(self):
        if self.length > 0:
            return self.values[0]
        else:
            return None

    def pop(self):
        self.length -= 1
        self.values[0] = self.values[self.length]
        del self.values[self.length]
        self.move_down(0)

    def get_raw_data(self):
        return self.values