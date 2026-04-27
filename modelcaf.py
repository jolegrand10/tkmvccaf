import logging # imported bib logging

logger = logging.getLogger("logCaf") # add a logger
logging.basicConfig(
    filename="logCaf.log",
    format="%(asctime)s %(message)s",
    level=logging.INFO)

class ModelCaf:

    BAREME = {
    #salaire:alloc
    500:400,
    1000:200,
    1500:150,
    2000:50,
    }
    def __init__(self, bareme = None):
        if bareme :
            self.bareme = ModelCaf.lire_bareme(bareme)
            logging.info("Bareme from caf.ini")
        else :
            self.bareme = ModelCaf.BAREME
            logging.info("Bareme from const in class ModelCaf")
    

    def caf(self, revenu: float) -> float:
        """ calcule le montant de l'allocation à partir du
            revenu net mensuel
        """
        for k in sorted(self.bareme.keys()):
            if revenu < k:
                return self.bareme[k]
        return 0.0
    

    def lire_bareme(nom_fichier):
        """ lire le fichier et renvoyer un dictionnaire bareme """
        #
        # initialiser un dico vide pour faire le bareme
        #
        b = {}
        with open(nom_fichier, "rt", encoding="utf-8") as f:
            for ligne in f:
                print(ligne) # debug
                s, a = ligne.split()
                s, a = float(s), float(a)
                b[s] = a
        return b
    
def main():
    """ un test pour la classe ModelCaf """
    mc = ModelCaf()
    assert(mc.caf(3000)==0.0)
    assert(mc.caf(0)==400.00)
    assert(mc.caf(500)==200.00)
    assert(mc.caf(1350)==150.00)
    mc = ModelCaf("caf.ini")
    assert(mc.caf(3000)==0.0)
    assert(mc.caf(0)==400.00)
    assert(mc.caf(500)==200.00)
    assert(mc.caf(1350)==150.00)
    print("Ok!")
    logging.info("Test Ok!")

if __name__ == '__main__':
    main()