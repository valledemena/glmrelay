import difflib
import sys
import unicodedata


def norm(path):
    t = open(path, encoding='utf-8').read()
    t = unicodedata.normalize('NFKD', t)
    t = ''.join(c for c in t if not unicodedata.combining(c))
    return t.split()


a = norm(sys.argv[1])  # archivada (transcripcion)
b = norm(sys.argv[2])  # canonica (GLM)
sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
ops = 0
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag != 'equal':
        ops += 1
        print(f"[{ops}] {tag}")
        print(f"    archivada: {' '.join(a[i1:i2])!r}")
        print(f"    canonica : {' '.join(b[j1:j2])!r}")
print(f"palabras: archivada {len(a)} / canonica {len(b)} / operaciones {ops}")
