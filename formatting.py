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
     "So I said goodnight.")
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec"

print "Here are the days:", days
print "Here are the months:", months

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm spilt\non a line."
backlash_cat = "I'm \\ a \\ cat"

fat_cat = """
I'll do a list:
\t* Cat Food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backlash_cat
print fat_cat