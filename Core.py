import re
import HT

HT_obj = HT.HT()


class Core:

    #  loading hash table
    def __init__(self):
        HT_obj.read()

    @staticmethod
    def make(inp, file_io, line, r_flag=False):

        # split input text to terms(words)
        terms = re.findall(r'\w+', inp.lower())

        for i in range(len(terms)):

            # finding chance of be a error for terms
            score = 0.0
            # search for term in hash table
            if HT_obj.bin_search(HT_obj.hash(terms[i])) == -1:
                score = 1
                if 0 < i < len(terms) - 1:
                    if HT_obj.bin_search(HT_obj.hash(terms[i - 1])) == -1 and len(terms[i - 1]) > 5:
                        score -= 0.5
                    if HT_obj.bin_search(HT_obj.hash(terms[i + 1])) == -1 and len(terms[i + 1]) > 5:
                        score -= 0.5

            # term is a error
            if score >= 0.5:
                sim = HT_obj.replace(terms[i])  # finding suggestions based on term
                # print outs on Terminal(Console) or output file
                if not r_flag:
                    print('_______________________')
                    print('The term "', terms[i], '" has spelling problem.')
                    print('Replace suggestions: ')
                    for j in sim:
                        print(j)
                else:
                    file_io.write('line ' + str(line) + ' .______________________' + '\n')
                    file_io.write('The term "' + terms[i] + '" has spelling problem.' + '\n')
                    file_io.write('Replace suggestions: ' + '\n')
                    for j in sim:
                        file_io.write(j + '\n')
