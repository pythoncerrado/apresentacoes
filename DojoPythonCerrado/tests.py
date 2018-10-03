import unittest
from main import Brainfuck

class BrainfuckTests(unittest.TestCase):

    def setUp(self):
        self.bf = Brainfuck()

    def test_ret_inc_cell(self):
        program = '+'
        cells, pointer = self.bf.brainfuck_program(program)
        self.assertEqual(cells[0], 1)

    def test_ret_inc_cell(self):
        program = '+++'
        cells, pointer = self.bf.brainfuck_program(program)
        self.assertEqual(cells[0], 3)

    def test_ret_dec_255_cell(self):
        program = '-'
        cells, pointer = self.bf.brainfuck_program(program)
        self.assertEqual(cells[0], 255)

    def test_ret_dec_cell(self):
        program = '+-'
        cells, pointer = self.bf.brainfuck_program(program)
        self.assertEqual(cells[0], 0)

    def test_ret_inc_dec_cell(self):
        program = '++-'
        cells, pointer = self.bf.brainfuck_program(program)
        self.assertEqual(cells[0], 1)

    def test_character(self):
        program = 'a'
        cells, pointer = self.bf.brainfuck_program(program)
        self.assertEqual(cells[0], 0)

    def test_increment_pointer(self):
        program = '<+'
        cells, pointer = self.bf.brainfuck_program(program)
        self.assertEqual(cells[1], 1)
        self.assertEqual(cells[0], 0)
        self.bf.pointer = 29999
        with self.assertRaises(Exception) as w:
            cells, pointer = self.bf.brainfuck_program(program)

    def test_decrement_pointer(self):
        program = '>+'
        with self.assertRaises(Exception) as w:
            cells, pointer = self.bf.brainfuck_program(program)
        self.bf.pointer = 1
        cells, pointer = self.bf.brainfuck_program(program)
        self.assertEqual(cells[0], 1)

    def test_get_input(self):
        test_string = 'a'
        program = ','
        func = lambda: test_string
        cells, pointer = self.bf.brainfuck_program(program, func)
        self.assertEqual(cells[0], 97)

    def test_output(self):
        test_string = 'a'
        program = ',.'
        func = lambda: test_string
        cells, pointer = self.bf.brainfuck_program(program, func)
        self.assertEqual(cells[0], ord('a'))
        self.assertEqual(self.bf.get_output())

if __name__ == '__main__':
    unittest.main()
