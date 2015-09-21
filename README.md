# py-mapzen-whosonfirst-names

Python tools for working with place names in Who's On First data

_Note that as of this writing the naming conventions for `wof` data are not reflected in the [whosonfirst-data](https://github.com/whosonfirst/whosonfirst-data) repository._

## Usage

### mapzen.whosonfirst.names.labels

```
import mapzen.whosonfirst.names

lbl = mapzen.whosonfirst.names.labels()
names = ("fin_p", "eng_s", "unk_v")

for n in names:
	print n

        n2 = lbl.convert(n, 'geoplanet', 'wof')
        print n2

        n3 = lbl.convert(n2, 'wof', 'subtags')
        print n3

        n4 = lbl.convert(n3, 'subtags', 'wof')
        print n4

        n5 = lbl.convert(n4, 'wof', 'geoplanet')
        print n5
```

Would yield:

```
fin_p
fin_x_prefered
fin-x-prefered
fin_x_prefered
fin_p
eng_s
eng_x_colloquial
eng-x-colloquial
eng_x_colloquial
eng_s
unk_v
und_x_variant
und-x-variant
und_x_variant
unk_v
```

## See also

* https://github.com/whosonfirst/py-mapzen-whosonfirst-languages
