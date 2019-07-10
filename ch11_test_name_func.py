# A PASSING TEST

import unittest  # importing unittest module
from ch11_name_func import get_formatted_name


class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('jans', 'joplin')
        self.assertEqual(formatted_name, "Jans Joplin")


unittest.main()
