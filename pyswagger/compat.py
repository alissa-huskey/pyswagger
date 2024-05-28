"""Compatability."""

try:
    from collections import MutableMapping
except ImportError:
    # Python 3.3+
    from collections.abc import MutableMapping
