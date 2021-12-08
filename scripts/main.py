#!/usr/bin/env python3
from flags import _flags
from tmp import _tmp
from translations import _t


def main():
    try:
        flag_lang = _flags.value(['--lang', '-l'])
        _t.load(flag_lang) if flag_lang else _t.load()
        _tmp.dir()

    except BaseException as ex:
        raise TypeError(ex)


if __name__ == '__main__':
    main()


# https://github.com/OSCAR-WOS/python-boilerplate
