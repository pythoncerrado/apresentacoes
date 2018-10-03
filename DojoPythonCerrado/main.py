class Brainfuck:
    def __init__(self):
        self.pointer = 0
        self.cells = [0] * 30000

    def inc_pointer(self):
        self.pointer += 1

    def dec_pointer(self):
        if self.pointer == 0:
            raise ValueError('Index out of range')
        else:
            self.pointer -= 1


    def inc_value(self):
        self.cells[self.pointer] += 1

    def dec_value(self):
        self.cells[self.pointer] -= 1
        if self.cells[self.pointer] < 0:
            self.cells[self.pointer] = 255

    def get_input(self, input=input):
        a = input()
        to_ascii = ord(a[0])
        self.cells[self.pointer] = to_ascii
        # get input from user?

    def get_output(self):
        #to_ascii = ord(a[0])
        print(chr(self.cells[self.pointer]))
        return(0)
        
    def brainfuck_program(self,program, param=None):
        for op in program:
            operators = {
                '+': self.inc_value,
                '-': self.dec_value,
                '<': self.inc_pointer,
                '>': self.dec_pointer,
                ',': self.get_input,
                '.': self.get_output
            }
            func = operators.get(op)
            if func is not None:
                if param is not None and op == ',':
                    func(param)
                else:
                    func()
        return (self.cells, self.pointer)
