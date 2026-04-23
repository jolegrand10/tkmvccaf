""" Module main.py pour l'application CAF avec
    tkinter en MVC """
import tkinter as tk
from modelcaf import ModelCaf
from viewcaf import ViewCaf
from controllercaf import ControllerCaf


def main():
    v = ViewCaf()
    m = ModelCaf()
    c = ControllerCaf(model=m, view=v)
    c.run()

if __name__ == '__main__':
    main()