import unittest
from unittest.mock import patch, call
import game


class TestGame(unittest.TestCase):

    # Patching get_random_number and get_user_input to both return 5
    @patch('game.get_random_number', return_value=5)
    @patch('game.get_user_input', side_effect=[3, 8, 5])
    def test_play(self, mock_input, mock_random):
        with patch('builtins.print') as mock_print:
            game.main()

        expected_calls =[call("Higher!"), call("Lower!"), call("You win!")]
        self.assertEqual(expected_calls, mock_print.call_args_list)
