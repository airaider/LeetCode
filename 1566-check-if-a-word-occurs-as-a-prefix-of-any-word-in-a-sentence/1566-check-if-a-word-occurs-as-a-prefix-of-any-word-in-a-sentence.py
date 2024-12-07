class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        word_index = sentence.split()
        for i, word in enumerate(word_index):
            if word.startswith(searchWord): return i+1
        return -1
        