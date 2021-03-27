# -----------------------------
# Created on 25th March, 2021
# By Naimish Mani B
# -----------------------------
'''
This module contains all classes required to train the
various classifiers.
'''


class LogisticRegression(object):
    def __init__(self):
        self.X = []
        self.y = []
        self.epochs = 0
        self.batchSize = 0
