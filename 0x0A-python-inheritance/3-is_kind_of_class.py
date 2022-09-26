#!/usr/bin/python3

"""Only Sub Class Of Module."""


def inherits_from(obj, a_class):
    """Check if obj is subclass of a_class."""
    return issubclass(type(obj), a_class)
