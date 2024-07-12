'''
open all_code_cells.txt and read it
split it into a split('----index----')
for each index, create a new file and write the contents of the index to the file. file names are index002.txt,index003.txt,index004.txt,etc.'''
import os
def write_code_cells():
    with open('test_scripts/code_cells/all_code_cells.txt','r') as f:
        data = f.read()
    data = data.split('----index----')
    for i in range(len(data)):
        with open('code_cells_txt/index'+str(i).zfill(3)+'.txt','w') as f:
            f.write(data[i])
if __name__ == '__main__':
    write_code_cells()
    print('done')            
            