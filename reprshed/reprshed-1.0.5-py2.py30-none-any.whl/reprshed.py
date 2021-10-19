# SPDX-License-Identifier: 0BSD
# Copyright 2021 Alexander Kozhevnikov <mentalisttraceur@gmail.com>

"""A toolshed for writing great ``__repr__`` methods quickly and easily."""

__all__ = ('pure', 'impure', 'raw')
__version__ = '1.0.5'


try:
    from _thread import get_ident as _thread_id
except ImportError:
    try:
        from thread import get_ident as _thread_id
    except ImportError:
        try:
            from dummy_thread import get_ident as _thread_id
        except ImportError:
            def _thread_id():
                return 0


_in_progress = set()


def _name(obj):
    return type(obj).__name__


def pure(*args, **kwargs):
    """Represent an object and its arguments as an unambiguous string.

    Arguments:
        self: An instance of a class - normally the ``self``
            argument of the ``__repr__`` method in a class.
            (This argument must be the first in ``*args``.)
        *args: Positional arguments that describe the instance.
        **kwargs: Keyword arguments that describe the instance.

    Returns:
        str: The representation of ``self`` and its arguments.
    """
    def pure(self, *args):
        return self, args
    self, args = pure(*args)
    repr_id = (id(self), _thread_id())
    if repr_id in _in_progress:
        return '<...>'
    try:
        _in_progress.add(repr_id)
        arguments = []
        for argument in args:
            arguments.append(repr(argument))
        for name, argument in kwargs.items():
            arguments.append('='.join((name, repr(argument))))
        return ''.join((_name(self), '(', ', '.join(arguments), ')'))
    finally:
        _in_progress.discard(repr_id)


def impure(*args, **kwargs):
    """Represent an object and its state as an unambiguous string.

    Arguments:
        self: An instance of a class - normally the ``self``
            argument of the ``__repr__`` method in a class.
            (This argument must be the first in ``*args``.)
        *args: Unnamed state that describes the instance.
        **kwargs: Named state that describes the instance.

    Returns:
        str: The representation of ``self`` and its state.
    """
    def impure(self, *args):
        return self, args
    self, args = impure(*args)
    repr_id = (id(self), _thread_id())
    if repr_id in _in_progress:
        return '<...>'
    try:
        _in_progress.add(repr_id)
        parts = [_name(self)]
        for argument in args:
            parts.append(repr(argument))
        for name, argument in kwargs.items():
            parts.append('='.join((name, repr(argument))))
        return ''.join(('<', ' '.join(parts), '>'))
    finally:
        _in_progress.discard(repr_id)


def raw(string):
    """Escape a string to make ``reprshed`` use it verbatim."""
    class _Raw(object):
        def __repr__(self):
            return string
        def __reduce__(self):
            return (raw, (string,))
    _Raw.__name__ = string
    return _Raw()
