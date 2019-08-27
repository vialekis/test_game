import unittest
import tictactoe

class MyCalcTest(unittest.TestCase):
    def test_validate_board(self):
        self.assertTrue(tictactoe.validate_board([[0, 0, 0],[0, 0, 0],[0, 0, 0]]))

    def test_validate_board1(self):
        self.assertTrue(tictactoe.validate_board([[1, 2, 3],[2, 1, 0],[2, 1, 1]]))

    def test_validate_board2(self):
        self.assertTrue(tictactoe.validate_board([[1, 2, 0],[2, 0, 0],[2, 1, 1]]))

    def test_validate_board3(self):
        self.assertTrue(tictactoe.validate_board([[1, 1, 0],[2, 1, 0],[2, 1, 1]]))

    def test_validate_board4(self):
        self.assertTrue(tictactoe.validate_board([[1,2,0,1],[2, 1, 0],[2, 2, 1]]))

    def test_finished(self):
        self.assertIn(tictactoe.game_finished([[1,2,0,1],[2, 1, 0],[2, 2, 1]]), [-1,0,1,2])

    def test_finished1(self):
        self.assertIn(tictactoe.game_finished([[1,2,0,],[1, 2, 0],[1, 2, 1]]), [-1,0,1,2])

    def test_finished2(self):
        self.assertIn(tictactoe.game_finished([[1,1,1],[2, 0, 2],[0, 2, 1]]), [-1,0,1,2])

    def test_finished3(self):
        self.assertIn(tictactoe.game_finished([[1,2,1],[2, 1, 1],[2, 2, 1]]), [-1,0,1,2])

    def test_render(self):
        self.assertIsInstance(tictactoe.render_board([[1,2,1],[2, 1, 1],[2, 2, 1]]), str)

    def test_render1(self):
        self.assertIsInstance(tictactoe.render_board([[1, 2], [2, 1, 1], [2, 2, 1]]), str)

    def test_render2(self):
        self.assertIsInstance(tictactoe.render_board([[0,0,3],[0, 0, 0],[0, 0, 0]]), str)

    def test_render3(self):
        self.assertIsInstance(tictactoe.render_board([[1,1,1],[2, 3, 3],[2, 1, 1]]), str)

if __name__ == "__main__":
    unittest.main()