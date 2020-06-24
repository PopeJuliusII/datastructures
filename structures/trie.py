class Trie:
    @staticmethod
    def trie(*words):
        root = {}
        for word in words:
            curr = root
            for char in word:
                curr = curr.setdefault(char, {})
            curr['count'] = curr.setdefault('count', 0) + 1
        return root
