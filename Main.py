import Core

print('Loading word list.')
Core_obj = Core.Core()  # loading dictionary.json file into hash table
print('Word list is loaded.')

inp = input('Do you want read a file?[Y/n]: ')

#  input text mode
if inp.lower() == 'n':
    while True:
        inp = input('Insert a text or exit(): ')

        if inp.lower() == 'exit()':
            break
        else:
            Core_obj.make(inp, None, 0, False)  # finding spelling problems and find suggestions

#  file mode
else:

    inp = input('Insert file dir: ')

    #  opening IO files
    file_r = open(inp, 'r', encoding='utf-8')
    file_w = open(inp + 'out.txt', 'w', encoding='utf-8')

    cc = 0
    #  make iterate on every line in input file
    for line in file_r:
        cc += 1
        err = Core_obj.make(line, file_w, cc, True)  # finding spelling problems and find suggestions

    #  closing IO files
    file_w.close()
    file_r.close()
    print('Done.')
