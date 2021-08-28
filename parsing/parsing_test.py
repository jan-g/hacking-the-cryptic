import pytest
import re

@pytest.mark.parametrize("given,then", [
    (r'a=1 b=2 c=hello d="hello world" e="\""',
     {"a":"1", "b":"2", "c":"hello", "d": "hello world", "e": '"'}),
])
def test_parse(given, then):
    assert parse(given) == then


R = re.compile(r"""
               (?P<key> \w+)
               =
               (?:
               ( [^"\s]* )            # non-quote stuff
               |
               "
               ( (?: [^"]* | \\\" )+ )
               "
               ) 
               
               (?: \s+|$ )            # spaces or EOS
               """, re.VERBOSE)


def parse(s):
    res = {}

    while (m := R.match(s)) is not None:
        print(m)
        res[m.group(1)] = m.group(2) or m.group(3).replace(r'\"', r'"')
        s = s[m.end():]
        print(s)

    return res
