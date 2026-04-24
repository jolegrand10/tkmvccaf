""" Module controllercaf.py  Controleur pour l'appli CAF en"""
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    filename="app.log"  # log dans un fichier
)
class ControllerCaf:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_command_calcul(self.calcul)

    def calcul(self):
        print("On calcule l'allocation maintenant")
        logging.info("Début du Calcul")
        # recupérer la valeur du salaire
        try :
            r = self.view.get_salaire()
            logging.debug(f"Salaire récupéré : {r=}")
        # appeler la fonction caf
            r = float(r)
            if r is None or r.strip()=="":
                raise ValueError("Champ vide")
            v = self.model.caf(r)
        #
        # mettre le résultat dans la vue
        #
            self.view.set_allocation(f"{v:.2f}")
            logging.info("Succès!")
        except TypeError as e:
            logging.warning(f'Erreur Type: {e}')

        except ValueError as e:
            logging.warning(f"Erreur Valeur : {e}")

        except Exception as e:
            logging.error(f'Erreur Autre: {e}')



    def run(self):
        try :
            self.view.run()
        except Exception as e :
            logging.error("Erreur éxécution : {e}")