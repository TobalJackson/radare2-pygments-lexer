from setuptools import setup

entry_points = """ 
[pygments.lexers]
r2highlight = r2highlight.radare2:Radare2Lexer
"""

setup(
    name = "r2highlight",
    version = "0.0.0",
    description = __doc__,
    author = "Tobal Jackson",
    packages = ['r2highlight'],
    entry_points = entry_points
)
