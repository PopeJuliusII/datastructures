from structures import Trie
import os
import unittest
import string
from collections import Counter


class TestTrie(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path = os.path.join(os.path.dirname(__file__), 'materials', 'How A Gardner May Get Rid Of Doormice.txt')
        with open(path, 'r') as f:
            f = f.read()
            peaches = ""
            for char in f:
                if char.lower() in string.ascii_lowercase + ' .':
                    if char != '.':
                        peaches += char.lower()
                        continue
                    peaches += ' '
        cls.peaches = peaches.split()
        cls.count, cls.trie = Counter(cls.peaches), Trie.trie(*cls.peaches)

    def test_trie(self):
        trie_list = [
            self.trie['r']['o']['s']['e']['t']['r']['e']['e']['count'],
            self.trie['b']['e']['e']['n']['count'],
            self.trie['a']['l']['l']['count'],
            self.trie['y']['o']['u']['r']['count'],
            self.trie['y']['o']['u']['count'],
            self.trie['p']['e']['a']['c']['h']['e']['s']['count'],
            self.trie['t']['h']['e']['count']
        ]
        counter_list = [
            self.count['rosetree'],
            self.count['been'],
            self.count['all'],
            self.count['your'],
            self.count['you'],
            self.count['peaches'],
            self.count['the']
        ]
        self.assertEqual(all(t == c for t, c in zip(trie_list, counter_list)), True)


if __name__ == '__main__':
    unittest.main()
