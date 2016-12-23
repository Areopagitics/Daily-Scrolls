import fileinput
import sys
import re

Books = {
    'Mt':       'Matthew'	,
    'Mk':       'Mark'	,
    'Lk':       'Luke'	,
    'Jn':       'John'	,
    'Acts':      'Acts'	,
    'Rom':      'Romans'	,
    "1 Cor":    '1 Corinthians'	,
    "2 Cor":    '2 Corinthians'	,
    'Gal':      'Galatians'	,
    'Eph':      'Ephesians'	,
    'Phil':     'Philippians'	,
    'Col':      'Colossians'	,
    '1 Thes':  '1 Thessalonians'	,
    '2 Thes':  '2 Thessalonians'	,
    '1 Tm':    '1 Timothy'	,
    '2 Tm':    '2 Timothy'	,
    'Titus'  :   'Titus'	,
    'Philem':   'Philemon'	,
    'Heb':      'Hebrews'	,
    'Js'   :    'James'	,
    '1 Pt':    '1 Peter'	,
    '2 Pt':    '2 Peter'	,
    '1 Jn':     '1 John'	,
    '2 Jn':     '2 John'	,
    '3 Jn':     '3 John'	,
    'Jude'   :   'Jude'	,
    'Rv':      'Revelation'	,
    'Gen':      'Genesis'	,
    'Ex':       'Exodus'	,
    'Lev':      'Leviticus'	,
    'Num':      'Numbers'	,
    'Deut':     'Deuteronomy'	,
    'Josh':     'Joshua'	,
    'Judg':     'Judges'	,
    'Ruth':     'Ruth'	,
    '1 Sam':    '1 Samuel'	,
    '2 Sam':    '2 Samuel'	,
    '1 Kgs':    '1 Kings'	,
    '2 Kgs':    '2 Kings'	,
    '1 Chr':    '1 Chronicles'	,
    '2 Chr':    '2 Chronicles'	,
    'Ezra':      'Ezra'	,
    'Neh':      'Nehemiah'	,
    'Tob':      'Tobit'	,
    'Jdt':      'Judith'	,
    'Esth':     'Esther'	,
    '1 Macc':   '1 Maccabees'	,
    '2 Macc':   '2 Maccabees'	,
    'Job'   :    'Job'	,
    'Ps':       'Psalms'	,
    'Prov':     'Proverbs'	,
    'Eccl':     'Ecclesiastes'	,
    'Song'   :   'Solomon'	,
    'Wis':      'Wisdom',
    'Sir':      'Sirach'	,
    'Is':       'Isaiah'	,
    'Jer':      'Jeremiah'	,
    'Lam':      'Lamentations'	,
    'Bar':      'Baruch'	,
    'Ez':     'Ezekiel'	,
    'Dan':      'Daniel'	,
    'Hos':      'Hosea'	,
    'Jl'  :    'Joel'	,
    'Am':       'Amos'	,
    'Ob':       'Obadiah'	,
    'Jon':      'Jonah'	,
    'Mic':      'Micah'	,
    'Nah':      'Nahum'	,
    'Hab':      'Habakkuk'	,
    'Zeph':     'Zephaniah'	,
    'Hag':      'Haggai'	,
    'Zech':     'Zechariah'	,
    'Mal':      'Malachi'	,

}



for line in fileinput.input("text.txt", inplace=1):
    try:
        m = re.search('(\d )?[A-z]+', line).group()
    except:
        pass
    if m in line:
        line = line.replace(m,Books[m])
    sys.stdout.write(line)



'''
o = open("output.txt","a")
for line in open("text.txt"):
    m = re.search('(\d )?[A-z]+', line).group()
    if m:
        new = Books[m]
        print new


    else:
        o.write(line)
o.close()


def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)


pattern = re.compile("<(\d{4,5})>")

for i, line in enumerate(open('test.txt')):
    for match in re.finditer(pattern, line):
        print 'Found on line %s: %s' % (i+1, match.groups())


size = os.stat(fn).st_size
f = open(fn)
data = mmap.mmap(f.fileno(), size, access=mmap.ACCESS_READ)

m = re.search(r"867-?5309", data)

o = open("output.txt","a") #open for append
for line in open("test.txt"):
   if "gggg" in line:
        o.write(line + "\n")
   else:
        o.write(line)
o.close()

'''
