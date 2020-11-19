"""
Code illustration: 8.12
Tkinter Class Hierarchy Inspect
Tkinter GUI Application Development Blueprints
"""
import tkinter
import inspect

print ('Class Hierarchy for Frame Widget')
for i, classname in enumerate(inspect.getmro(tkinter.Frame)):
    print('{}: {}'.format(i, classname))

print ('Class Hierarchy for Toplevel')
for i, classname in enumerate(inspect.getmro(tkinter.Toplevel)):
    print ('{}:{}'.format(i, classname))

print ('Class Hierarchy for Tk')
for i, classname in enumerate(inspect.getmro(tkinter.Tk)):
    print ('{}: {}'.format(i, classname))
