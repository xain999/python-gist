# -*- coding: utf-8 -*-

"""
A simple way to convert a ctype.POINTER into an array.
This is needed if we get ctype.POINTER as a callback
from the C function call.
"""

import ctypes

class EventResult(ctypes.Structure):
  _fields_ = [
    ("status", ctypes.c_ulong),
    ("type", ctypes.c_ulong)
  ]

x = EventResult()               # creating simple object
obj = ctypes.pointer(x)         # getting its pointer
print obj                       # this is the object that I get in callback

size = 1                        # size of array
ArrayType = (EventResult * 1)   # type of array

# casting object ptr to array ptr. In C, EventResult** arr
arr = ctypes.cast(obj, ctypes.POINTER(ArrayType))
print arr
item = arr[0]                   # dereference to the array
print item

for i in item:
	print i                   	# access first item of the array
	print i.status            	# equals to x.status
  
