r"""
>>> check_output("int x;  // simple comment")
int x;
>>> check_output("int x;///comment")
int x;
>>> check_output("int/*hello*/x;")
int x;
>>> check_output("int/*\ncomment\n*/x;/*second comment*/")
int x;
>>> check_output("float x = 0.0;")
float x=0.0;

>>> check_output("a = a - -1")
a=a- -1
>>> check_output("a = a-- -1")
a=a---1
>>> check_output("a = a- --a")
a=a- --a
>>> check_output("#define x <")
#define x <
>>> check_output("#define x(y) (y)")
#define x(y)(y)

>>> check_output("word .0")
word .0
>>> check_output("word.attribute")
word.attribute
>>> check_output("{{}}")
{{}}
"""

import doctest
import lib


def check_output(s):
    print(lib.serialize(lib.tokenize(s)))


doctest.testmod()
