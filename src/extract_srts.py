from os import listdir, mkdir
from os.path import isfile, join
import sys
import rarfile
import chardet

if __name__ == '__main__':
  rarpath = sys.argv[1]
  targetpath = sys.argv[2]
  rarfiles = (f for f in listdir(rarpath))
  
  for file in rarfiles:
    print file
    dest = None

    try:
      with rarfile.RarFile(join(rarpath, file)) as rar:
        if rar.needs_password():
          print 'Needs passwords..'
          continue
        for f in rar.infolist():
          if f.filename.endswith('.srt') and not f.isdir():
            if dest is None:
              dest = join(targetpath, file)
              mkdir(dest)
            rar.extract(f, dest)
            
    except Exception as e:
      print 'ERROR:', e
  
