class Solution(object):
    def oddString(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        d = lambda word: [ord(w2) - ord(w1) for w1, w2 in zip(word, word[1:])]
        difference = [ d(word)for word in words]
        print(difference)
        index = [difference.index(i) for i in difference if difference.count(i) == 1]
        print(index)
        if not index: return None
        return words[index[0]]
