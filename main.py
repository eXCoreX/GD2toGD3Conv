import re
import glob


def process_files():
    pattern1 = re.compile(r'(((?:"\.)|(?:[^.]))(get_node\("(.*?)"\)(\.?)))')
    pattern2 = re.compile(r'([^.])get_parent\((.*?)\)')
    pattern3 = re.compile(r'"\.\$"')
    gdFilePaths = []
    for filename in glob.iglob('**/*.gd', recursive=True):
        gdFilePaths.append(filename)
    countf = 0
    countl = 0
    for filePath in gdFilePaths:
        file = open(filePath, 'r')
        a = file.read()
        file = open(filePath, 'w')
        a = pattern2.sub(r'\1$".."', a)
        cc = pattern1.findall(a)
        if len(cc) != 0:
            for e in cc:
                print('%-60s' % e[2], 'file: %s' % filePath)
                countl += 1
        temp = a
        a = pattern1.sub(r'\2$"\4"\5', a)
        while temp != a:
            temp = a
            a = pattern1.sub(r'\2$"\4"\5', a)
        a = pattern3.sub('/', a)
        #print(a)
        file.write(a)
        countf += 1
    print('files processed: %d' % countf)
    print('functions refactored: %d' % countl)

if __name__ == '__main__':
    process_files()