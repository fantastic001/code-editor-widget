
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

class CodeHighlighter(QSyntaxHighlighter):
    
    def __init__(self, parent):
        
        kw_format = QTextCharFormat()
        kw_format.setForeground(QBrush(QColor(255, 0, 120)))

        self.rules = []
        keywords = ["char", "class", "const", "int", "double", "float", "long", "private", "public", "void", "unsigned", "short"]
        for kw in keywords:
            self.rules.append((QRegExp(kw), kw_format))

        quotationFormat = QTextCharFormat()
        quotationFormat.setForeground(QBrush(QColor(120, 255, 120)))

        self.rules.append((QRegExp("\".*\""), quotationFormat))
        

    def highlightBlock(self, text):
        
        for r in self.rules:
            exp = QRegExp(r[0])
            index = exp.indexIn(text)
            while index >= 0:
                length = exp.matchedLength();
                self.setFormat(index, length, r[1])
                index = exp.indexIn(text, index + length)


