#!/usr/bin/python
# -*- coding: utf-8 -*-

formatter = " %r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)

print formatter % (
     "I had this thing.",
     "That you could right up time",
     "but it did't sing",
     "SO I said goodnight.")