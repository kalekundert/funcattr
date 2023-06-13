"""
Assign attributes to functions using a decorator.
"""

__version__ = '0.0.0'

def annotate(**attrs):

    def decorator(f):
        for k, v in attrs.items():
            setattr(f, k, v)
        return f

    return decorator

