class ModelCaf:

    BAREME = {
    #salaire:alloc
    500:400,
    1000:200,
    1500:150,
    2000:50,
    }

    def caf(self, revenu: float, bareme=None) -> float:
        """ calcule le montant de l'allocation à partir du
            revenu net mensuel
        """
        if bareme == None:
            bareme = ModelCaf.BAREME
        for k in sorted(bareme.keys()):
            if revenu < k:
                return bareme[k]
        return 0.0
    
def main():
    """ un test pour la classe ModelCaf """
    mc = ModelCaf()
    assert(mc.caf(3000)==0.0)
    assert(mc.caf(0)==400.00)
    assert(mc.caf(500)==200.00)
    assert(mc.caf(1350)==150.00)
    print("Ok!")

if __name__ == '__main__':
    main()