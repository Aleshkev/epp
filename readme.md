# EPP – automatic C++ code improvements

> The vision: to make people's lives better. \
> Please see attachment #1 for the list of aforementioned people.

This project is inspired by BrutBurger's [e](https://github.com/BrutBurger/e), but I also always wanted an automatic C++ code improvement tool.

## Installation

1. Install Python 3.7 or later.
2. Download the contents of this repository (e.g. by `git clone`).
3. `cd` to the directory where `epp.py` is.
4. `pip install -r requirements.txt` (with `pip` from the Python 3.7+ version).
5. `python ./epp.py --help` should now work (with `python` from the Python 3.7+ version).

If the steps above fail, _you_ failed.

## Improve Whitespace

The basic, least broken, functionality is to compress code by removing unnecessary spaces and comments: `./epp.py ./example.cpp` will convert code into something like this:

```cpp
#include <bits/stdc++.h>
using namespace std;template<typename T>struct Rectangle{pair<T,T>start,stop;Rectangle(T,T,T,T);};template<typename T>Rectangle<T>::Rectangle(T start_x,T start_y,T stop_x,T stop_y):start(start_x,start_y),stop(stop_x,stop_y){}template<typename T>ostream&operator<<(ostream&o,const Rectangle<T>&r){o<<"["<<r.start.first<<", "<<r.start.second<<", "<<r.stop.first<<", "<<r.stop.second<<"]";return o;}template<typename T>T area(Rectangle<T>r){return abs(r.stop.first-r.start.first)*abs(r.stop.second-r.start.second);}int main(){Rectangle<intmax_t>r(0,0,1,1);cout<<area(r)<<endl;}
```

This not only makes your code run faster for, um, obvious reasons, but also more readable: by fitting more code on the screen at once, you can read it many times faster.

## Automated Refactoring

When writing some C++ code, you may accidentally use some variable names like `i` as the counter in your `for` loop – this is a bad practice as you can't tell what the variable does without reading the whole program. Luckily, you can fix this easily with `./epp.py -r`. This will also name all the constants, purging all unnamed "magic numbers" from your code with no effort on your part.

```cpp
#define var_0 ", "
#define var_1 "["
#define var_2 "]"
#define var_3 .first
#define var_4 .second
#define var_5 .start
#define var_6 .stop
#define var_7 0
#define var_8 1
#define var_9 Rectangle
#define var_10 T
#define var_11 abs
#define var_12 area
#define var_13 const
#define var_14 cout
#define var_15 endl
#define var_16 int
#define var_17 intmax_t
#define var_18 main
#define var_19 namespace
#define var_20 o
#define var_21 operator
#define var_22 ostream
#define var_23 pair
#define var_24 r
#define var_25 return
#define var_26 start
#define var_27 start_x
#define var_28 start_y
#define var_29 std
#define var_30 stop
#define var_31 stop_x
#define var_32 stop_y
#define var_33 struct
#define var_34 template
#define var_35 typename
#define var_36 using
#include <bits/stdc++.h>
var_36 var_19 var_29;var_34<var_35 var_10>var_33 var_9{var_23<var_10,var_10>var_26,var_30;var_9(var_10,var_10,var_10,var_10);};var_34<var_35 var_10>var_9<var_10>::var_9(var_10 var_27,var_10 var_28,var_10 var_31,var_10 var_32):var_26(var_27,var_28),var_30(var_31,var_32){}var_34<var_35 var_10>var_22&var_21<<(var_22&var_20,var_13 var_9<var_10>&var_24){var_20<<var_1<<var_24 var_5 var_3<<var_0<<var_24 var_5 var_4<<var_0<<var_24 var_6 var_3<<var_0<<var_24 var_6 var_4<<var_2;var_25 var_20;}var_34<var_35 var_10>var_10 var_12(var_9<var_10>var_24){var_25 var_11(var_24 var_6 var_3-var_24 var_5 var_3)*var_11(var_24 var_6 var_4-var_24 var_5 var_4);}var_16 var_18(){var_9<var_17>var_24(var_7,var_7,var_8,var_8);var_14<<var_12(var_24)<<var_15;}
```

## Verification

Use `-v` flag to "verify" output. This will print some errors if the output doesn't compile, but also possibly in other cases, in which you should feel free to ignore them.

It requires some `g++` to be globally available, but sometimes can't detect it anyway or passes invalid arguments, in which cases you are lucky to be able to practice your attention to detail by manually verifying output.

## Autonomous Operator Refactoring

Sometimes you get annoyed by how inconvenient it is to write, for example, `~` on standard keyboard. But I have a solution just for you – it's possible to rename operators too! (With `-r -o`.)

```cpp
#define var_0 ", "
#define var_1 "["
#define var_2 "]"
#define var_3 &
#define var_4 (
#define var_5 )
#define var_6 *
#define var_7 ,
#define var_8 -
#define var_9 .first
#define var_10 .second
#define var_11 .start
#define var_12 .stop
#define var_13 0
#define var_14 1
#define var_15 :
#define var_16 ::
#define var_17 ;
#define var_18 <
#define var_19 <<
#define var_20 >
#define var_21 Rectangle
#define var_22 T
#define var_23 abs
#define var_24 area
#define var_25 const
#define var_26 cout
#define var_27 endl
#define var_28 int
#define var_29 intmax_t
#define var_30 main
#define var_31 namespace
#define var_32 o
#define var_33 operator
#define var_34 ostream
#define var_35 pair
#define var_36 r
#define var_37 return
#define var_38 start
#define var_39 start_x
#define var_40 start_y
#define var_41 std
#define var_42 stop
#define var_43 stop_x
#define var_44 stop_y
#define var_45 struct
#define var_46 template
#define var_47 typename
#define var_48 using
#define var_49 {
#define var_50 }
#include <bits/stdc++.h>
var_48 var_31 var_41 var_17 var_46 var_18 var_47 var_22 var_20 var_45 var_21 var_49 var_35 var_18 var_22 var_7 var_22 var_20 var_38 var_7 var_42 var_17 var_21 var_4 var_22 var_7 var_22 var_7 var_22 var_7 var_22 var_5 var_17 var_50 var_17 var_46 var_18 var_47 var_22 var_20 var_21 var_18 var_22 var_20 var_16 var_21 var_4 var_22 var_39 var_7 var_22 var_40 var_7 var_22 var_43 var_7 var_22 var_44 var_5 var_15 var_38 var_4 var_39 var_7 var_40 var_5 var_7 var_42 var_4 var_43 var_7 var_44 var_5 var_49 var_50 var_46 var_18 var_47 var_22 var_20 var_34 var_3 var_33 var_19 var_4 var_34 var_3 var_32 var_7 var_25 var_21 var_18 var_22 var_20 var_3 var_36 var_5 var_49 var_32 var_19 var_1 var_19 var_36 var_11 var_9 var_19 var_0 var_19 var_36 var_11 var_10 var_19 var_0 var_19 var_36 var_12 var_9 var_19 var_0 var_19 var_36 var_12 var_10 var_19 var_2 var_17 var_37 var_32 var_17 var_50 var_46 var_18 var_47 var_22 var_20 var_22 var_24 var_4 var_21 var_18 var_22 var_20 var_36 var_5 var_49 var_37 var_23 var_4 var_36 var_12 var_9 var_8 var_36 var_11 var_9 var_5 var_6 var_23 var_4 var_36 var_12 var_10 var_8 var_36 var_11 var_10 var_5 var_17 var_50 var_28 var_30 var_4 var_5 var_49 var_21 var_18 var_29 var_20 var_36 var_4 var_13 var_7 var_13 var_7 var_14 var_7 var_14 var_5 var_17 var_26 var_19 var_24 var_4 var_36 var_5 var_19 var_27 var_17 var_50
```

This doesn't work in many cases and frequently produces something uncompilable. It's recommended to always use this with `-v`.

## Performance

As great as you would expect. The processing was O(n²), until I placed an arbitrary limit of 2048 characters on any single token. This brilliant optimization made it possible to process as much as more than about one file per second.

## Reporting breakage

The program doesn't work in some well-known cases:

- with some preprocessor directives – that's hard to repair, please don't report that;
- with some C++17 and later features – I can't use them so neither should you, please don't report that;
- with some features removed in C++11 – you shouldn't use them, please don't report that;
- with `-r` flag – don't use it if you can't handle some broken output, please don't report that.

If the output is uncompilable or compiles to something different than source despite the input meeting none of the above conditions, I consider that a noteworthy bug and please report it in the Issues.

## Internals

"Wow, I just noticed this produces correct output for `x-- -x` and `x- --x`! This must use some professionally written tokenizer, using reference grammar!" No, I just hacked together some rules that seemed right. The rules are regexes or giant walls of conditionals.

## TODO

- [ ] add more innovative naming schemes than `var_{i}`
- [ ] add new option to arrange source code into arbitrary shapes (that's why the tokenizer already prefers shorter tokens where possible)
    ```cpp
    // Arbitrary shape.
    using       namespace std;tem\
    plate<      typename T>struct
    /****/      Rectangle{pair<T,T
    >start,     stop;Re\
    ctangle     (T,T,T
    ,T);};      template
    <typename T>Rectangle<T>::Rec\
    tangle(T start_x,T start_y,T \
    stop_x,T stop_y):start(start_x
    ```
- [ ] make code improvements not be reversible with `g++ -E` and autoformatter – that's a hard one:
  - [ ] detect usercode declarations and rename them completely, leaving no reference to the old name behind
  - [ ] that's impossible to implement with current approach, so throw away all the code and rewrite everything
- [x] don't throw away all the code
- [ ] rewrite readme.md to be sane
