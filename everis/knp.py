from itertools import groupby
from collections import namedtuple
from pprint import pprint as pp
 
def anyvalidcomb(items,  val=0, wt=0):
    ' All combinations below the maxwt '
    if not items:
        yield [], val, wt
    else:
        this, *items = items            # car, cdr
        for n in range(this.number+1):
            v = val + n*this.value
            w = wt  + n*this.weight
            if w > maxwt:
                break
            for c in anyvalidcomb(items, v, w):
                yield [this]*n + c[COMB], c[VAL], c[WT]
 
maxwt = 600
COMB, VAL, WT = range(3)
Item  = namedtuple('Items', 'name weight value number')
items = [ Item(*x) for x in
          (
            ("map", 9, 150, 1),
            ("compass", 13, 35, 1),
            ("water", 153, 200, 3),
            ("sandwich", 50, 60, 2),

           ) ]  
 
bagged = max( anyvalidcomb(items), key=lambda c: (c[VAL], -c[WT])) # max val or min wt if values equal
print("Bagged the following %i items\n  " % len(bagged[COMB]) +
      '\n  '.join('%i off: %s' % (len(list(grp)), item.name)
                  for item,grp in groupby(sorted(bagged[COMB]))))
print("for a total value of %i and a total weight of %i" % bagged[1:])