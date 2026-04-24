""" Module controllercaf.py  Controleur pour l'appli CAF en"""
import logging

logger = logging.getLogger("logCaf") # add a logger


class ControllerCaf:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_command_calcul(self.calcul)

    def calcul(self):
        logger.info("Début du calcul de l'allocation")
        # recupérer la valeur du salaire
        r = self.view.get_salaire()
        r = r.strip()
        logger.debug(f"Salaire récupéré : {r=}")
        try:
            if r is None or r == "":
                raise ValueError("Champ salaire vide")
            r = float(r)
        except ValueError as e:
            logger.warning(f"'{r}' est un salaire incorrect parce que : {e}")
            #
            # mettre un signal à la place du résultat
            #
            self.view.set_allocation("???")
        else:
            #
            # appeler la fonction caf
            #
            v = self.model.caf(r)
            #
            # mettre le résultat dans la vue
            #
            self.view.set_allocation(f"{v:.2f}")
            logger.info(f"Allocation calculée : {v:.2f}")

    def run(self):
        self.view.run()
