import bsdiff4
import shutil
from pathlib import Path

for path in Path('./nonroot/Arch').rglob('*.apk'):
    bsdiff4.file_diff(str(path).replace('nonroot', 'root'), path, './patches/Arch/' + path.name.replace('.apk','.bsdiff'))

for path in Path('./nonroot/Language').rglob('*.apk'):
    bsdiff4.file_diff(str(path).replace('nonroot', 'root'), path, './patches/Language/' + path.name.replace('.apk','.bsdiff'))

for path in Path('./nonroot/Theme').rglob('*.apk'):
    bsdiff4.file_diff('base.apk', path, './patches/Theme/' + path.name.replace('.apk','.bsdiff'))

for path in Path('./root/Theme').rglob('*.apk'):
    bsdiff4.file_diff('base.apk', path, './patches/root/' + path.name.replace('.apk','.bsdiff'))

for path in Path('./patches').rglob('*.bsdiff'):
    shutil.copy(path, './patches/' + str(path).replace('/', '-')[8:])
