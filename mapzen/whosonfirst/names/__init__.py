# https://pythonhosted.org/setuptools/setuptools.html#namespace-packages
__import__('pkg_resources').declare_namespace(__name__)

class labels:

    def __init__(self):
        pass

    def convert(self, label, source, dest):

        if dest == 'geoplanet':
            return self.to_geoplanet(label, source)

        elif dest == 'wof':
            return self.to_wof(label, source)

        elif dest == 'subtags':
            return self.to_subtags(label, source)
            
        else:
            raise Exception, "unknown convert source"

    def to_subtags(self, label, source):

        if source == 'geoplanet':

            lang, suffix = label.split("_")
    
            if lang == 'unk':
                lang = 'und'
            
            suffix = self.geoplanet_suffix_to_wof_suffix(suffix)
            return "%s-x-%s" % (lang, suffix)
        
        elif source == 'wof':
            return label.replace("_", "-")

        else:
            raise Exception, "unknown source"

    def to_wof(self, label, source):

        if source == 'geoplanet':

            label = self.to_subtags(label, source)
            return self.to_wof(label, 'subtags')

        elif source == 'subtags':
            return label.replace("-", "_")

        else:
            raise Exception, "unknown source"

    def to_geoplanet(self, label, source):

        if source == 'wof':

            parts = label.split("_")
            suffix = parts.pop()

            lang = parts[0]

            if lang == 'und':
                lang = 'unk'

            suffix = self.wof_suffix_to_geoplanet_suffix(suffix)
            return "%s_%s" % (lang, suffix)

        elif source == 'subtag':
            label = self.to_geoplanet(label, 'wof')
            return self.to_subtags(label, 'wof')

        else:
            raise Exception, "unknown source"
            
    def geoplanet_suffix_map(self):

        map = {
            'p': 'preferred',
            's': 'colloquial',
            'v': 'variant',
            'q': 'preferred',
        }
    
        return map
    
    def geoplanet_suffix_to_wof_suffix(self, s):

        map = self.geoplanet_suffix_map()
        return map.get(s, 'unknown')

    def wof_suffix_to_geoplanet_suffix(self, s):

        map = self.geoplanet_suffix_map()

        for k, v in map.items():

            # this should never happen but measure twice and all that
            # (20150928/thisisaaronland)

            if v == s and k == 'q':
                return 'p'
            elif v == s:
                return k
            else:
                continue

        return "u"

if __name__ == '__main__':

    l = labels()
    names = ("fin_p", "eng_s", "unk_v")

    for n in names:
        print n

        n2 = l.convert(n, 'geoplanet', 'wof')
        print n2

        n3 = l.convert(n2, 'wof', 'subtags')
        print n3

        n4 = l.convert(n3, 'subtags', 'wof')
        print n4

        n5 = l.convert(n4, 'wof', 'geoplanet')
        print n5

