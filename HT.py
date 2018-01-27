from json import load
from difflib import SequenceMatcher

wl = {}
wl_sk = []
s_flag = True


class HT:

    def read(self):

        global wl, wl_sk
        DL = {}
        try:
            file = open('dictionary.json', 'r', encoding='utf-8')  # open dictionary file
            DL = load(file)  # load dict-words in dict{} data type
            file.close()  # close the file
            for i in DL:
                wl[self.hash(i)] = i  # replace word with hash value
            DL.clear()  # clear temporary memory
            wl_sk = list(wl.keys())
            wl_sk = self.Qsort(wl_sk, 0, len(wl_sk) - 1)  # sorting hash values by Quick sort
            wl_sk.sort()

        except FileNotFoundError as e:
            print('File IO dose not work fine.')

    # convert word(term) to hash value
    @staticmethod
    def hash(word):
        Hval = 5381
        for char in word.lower():
            Hval = ((Hval << 5) + Hval) + ord(char)

        return Hval

    # search for word(term) in hash table
    @staticmethod
    def bin_search(word):

        # split space in two peaces
        f_flag = -1
        l2 = len(wl_sk) // 2
        # search in half of table
        if wl_sk[l2] > word:
            for i in range(0, l2 + 1):
                if wl_sk[i] == word:
                    f_flag = i
                    break
        elif wl_sk[l2] < word:
            for i in range(l2 - 1, len(wl_sk)):
                if wl_sk[i] == word:
                    f_flag = i
                    break
        else:
            f_flag = l2

        return f_flag

    # Quick sort method
    def Qsort(self, ls, start, end):

        global s_flag
        if (start < end) and s_flag:  # end the progress with sorting
            pivot = self.partition(ls, start, end)
            if abs(pivot - start) > 10 or start == 0:
                self.Qsort(ls, start, pivot - 1)
            else:
                s_flag = False  # end the progress with small partition size
            if abs(pivot - end) > 10 or pivot == 0:
                self.Qsort(ls, pivot + 1, end)
            else:
                s_flag = False
        return ls

    # make partition for quick sort
    @staticmethod
    def partition(ls, start, end):
        pivot = ls[start]
        lit = start + 1
        rit = end
        done = False
        while not done:
            while lit <= rit and ls[lit] <= pivot:
                lit = lit + 1
            while ls[rit] >= pivot and rit >= lit:
                rit = rit - 1
            if rit < lit:
                done = True
            else:
                temp = ls[lit]
                ls[lit] = ls[rit]
                ls[rit] = temp

        temp = ls[start]
        ls[start] = ls[rit]
        ls[rit] = temp
        return rit

    # find the suggestions based on term(spell error one in text)
    @staticmethod
    def replace(word):

        sw = {}
        for i in wl:
            if len(wl[i]) > 1:
                if (wl[i][0] == word[0] or wl[i][1] == word[1]) and abs(len(wl[i]) - len(word)) < 5:
                    sw[wl[i]] = SequenceMatcher(None, wl[i], word).ratio()  # give the word score by similarity

        # find the 3 best words( the most similar ones)
        res = []
        for w in sorted(sw, key=sw.get, reverse=True):
            res.append(w)
            if len(res) >= 3:  # you can change 3 for change number of suggestions
                break

        return res
