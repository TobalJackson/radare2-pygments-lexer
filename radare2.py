# -*- coding: utf-8 -*-
"""
    pygments.lexers.radare2
    ~~~~~~~~~~~~~~~~~~~~~~

    Lexers for Radare2 commandline output and Visual Mode.

"""

from pygments.lexer import RegexLexer, bygroups, include, words
from pygments.token import *

__all__ = ['Radare2Lexer']

class Radare2Lexer(RegexLexer):
    name = 'Radare2'
    aliases = ['r2', 'radare2']
    filenames = []

    tokens = {
        'root': [
            (r'\n', Text),
            (r'^\[', Text, 'cmdprompt'),
            (r'0[Xx]',String, 'addroutput'),
            (r'^/|\||\\', Keyword, 'pdoutput'),
            (r'^[^[]', Text, 'stroutput')
        ],

        'pdoutput': [
            (r'/|\||\\', Keyword),
            (r' ', Text),
            (r';$', Text),
            (r',', Operator),
            (r';', Comment, 'comment'),
            (r'(\()(.+?)(\))', bygroups(Text, Operator, Text)),
            (r'([A-Za-z]{3})(\.)([A-Za-z]{3})(\.)(\w+)', bygroups(Keyword, Operator, Keyword, Operator, Text)),
            (r'([A-Za-z]{3})(\.)(\w+)', bygroups(Keyword, Operator, Text)),
            (r'\(\)', Text),
            (r'(0[Xx][0-9a-f]{8,})([ ]+)([0-9a-f]+)([ ]+)', bygroups(String, Text, Text, Text)),
            include('stackops'),
            include('arithmeticops'),
            include('ipops'),
            include('otherops'),
            include('registers'),
            (r'0[Xx][0-9a-f]+', Number.Hex),
        ],

        'registers': [
            (words(('esp', 'ebp', 'eax', 'ebx', 'ecx', 'edx')),
            Text)
        ],

        'comment': [
            (r'.+$', Comment, '#pop')
        ],

        'cmdprompt': [
            (r'(0[xX][0-9a-f]+)(\])(>)(\s+)(\w+)?(.*)$', bygroups(Number.Hex, Text, Operator, Text, Name.Function, Text)),
            (r'.+$', Text)
        ],

        'addroutput': [
            (r'([0-9a-f]+)(\s{2})(.+)(\s{2})(.+)$', bygroups(String, Text, Number.Hex, Text, Text)),
            #(r'^\[', Text, '#pop'),
            #(r'(0[Xx][0-9a-f])(\s+)(.+)$', bygroups(Number.Hex, Text, Text))
        ],

        'stroutput': [
            (r'[A-Za-z%]+', Text),
            (r' ', Text),
            (r'[0-9a-f]+', Number.Hex),
            (r'[.:]', Operator),
        ],

        'otherops': [
            (words(('nop', 'dword', 'local_', '[', 'h]', '-')),
            Text)
        ],

        'stackops': [
            (words(('push', 'pop'), prefix=r'\b', suffix=r'\b'),
            Keyword)
        ],

        'arithmeticops': [
            (words(('leave', 'mov', 'lea', 'add', 'sub', 'imul', 'mul', 'shl', 'shr', 'sar', 'sal'), suffix=r'\b', prefix=r'\b'),
            Operator)
        ],

        'ipops': [
            (words(('jmp', 'jne', 'jae', 'jbe', 'call', 'ret'), suffix=r'\b', prefix=r'\b'),
            Name.Function)
        ]
    }

