""" Module main.py pour l'application CAF avec
    tkinter en MVC """
import tkinter as tk
import logging # imported bib logging
from modelcaf import ModelCaf
from viewcaf import ViewCaf
from controllercaf import ControllerCaf


logger = logging.getLogger("logCaf") # add a logger
logging.basicConfig(
    filename="logCaf.log",
    format="%(asctime)s %(message)s",
    level=logging.INFO)

def main():
    logging.info("Demarrage")
    v = ViewCaf()
    m = ModelCaf()
    c = ControllerCaf(model=m, view=v)
    c.run()

if __name__ == '__main__':
    main()