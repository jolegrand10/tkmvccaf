""" Module controllercaf.py  Controleur pour l'appli CAF en"""
class ControllerCaf:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_command_calcul(self.calcul)

    def calcul(self):
        print("On calcule l'allocation maintenant")
        #
        # recupérer la valeur du salaire
        #
        r = self.view.get_salaire()
        print(f"{r=}")
        #
        # appeler la fonction caf
        #
        v = self.model.caf(r)
        #
        # mettre le résultat dans la vue
        #
        self.view.set_allocation(f"{v:.2f}")


    def run(self):
        self.view.run()