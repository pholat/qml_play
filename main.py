#!/bin/python3

import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QGuiApplication, QSyntaxHighlighter, QTextDocument, QColor
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType


def tch_format(fore, bg=None, weight=None):
    ret = QtGui.QTextCharFormat()
    ret.setForeground(fore)
    if weight is not None:
        ret.setFontWeight(weight)
    if bg is not None:
        ret.setBackground(bg)
    return ret


js_patterns = {
    "string": {
        "reg": '"((\\\\")|[^"\\\\])*"',  # anything in "" including \"
        "fmt": tch_format(QtCore.Qt.blue)
    },
    "key": {
        "reg": '"((\\\\")|[^"\\\\])*"\s*:',
        "fmt": tch_format(QtCore.Qt.blue, weight=QtGui.QFont.Bold)
    },
    "num": {
        "reg": "\d+",
        "fmt": tch_format(QtCore.Qt.darkBlue)
    },
    "type": {
        "reg": "(true)|(false)|(null)",
        "fmt": tch_format(QtCore.Qt.red)
    },
    "container": {
        "reg": "[\[\]\{\}]",
        "fmt": tch_format(QtCore.Qt.darkCyan)
    }
}


class Highlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(Highlighter, self).__init__(parent)

    def highlightBlock(self, text):
        self.setFormat(0, len(text), tch_format(QtCore.Qt.red, weight=QtGui.QFont.Bold))
        for key in js_patterns:
            expression = QtCore.QRegExp(js_patterns[key]["reg"])
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, js_patterns[key]["fmt"])
                index = expression.indexIn(text, index + length)

def print_child(el):
    print(" " * 2 * print_child.max + "type: {}".format(type(el)))
    print(" " * 2 * print_child.max + "name: {}".format(el.objectName()))
    print_child.max += 1
    try:
        for subel in el.children():
            print_child(subel)
    except TypeError:
        pass
    print_child.max -= 1
print_child.max = 0


def child_selector(children, ftype):
    for ch in children:
        if type(ch) is ftype:
            return ch
    return None

if __name__ in "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.load("main.qml")
    print_child(engine.rootObjects()[0])
    json_view = child_selector(engine.rootObjects()[0].findChild(QObject, "text_view").children(), QTextDocument)
    try:
        with open("main.json") as fp:
            json_view.setPlainText(fp.read())
    except FileNotFoundError as err:
        print("no file main.json")
    el = Highlighter(json_view)
    engine.quit.connect(app.quit)
    sys.exit(app.exec_())
