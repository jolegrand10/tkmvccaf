import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from modelcaf import ModelCaf

def test_revenu_eleve():
    mc = ModelCaf()
    assert mc.caf(3000) == 0.0

def test_revenu_zero():
    mc = ModelCaf()
    assert mc.caf(0) == 400.0

def test_revenu_limite():
    mc = ModelCaf()
    assert mc.caf(500) == 200.0

def test_revenu_intermediaire():
    mc = ModelCaf()
    assert mc.caf(1350) == 150.0


# TEST avec caf.ini
def test_caf_avec_fichier_ini():
    mc = ModelCaf()
    bareme = {}

    chemin = Path(__file__).resolve().parents[1] / "caf.ini"

    with open(chemin, "r") as fichier:
        for ligne in fichier:
            salaire, allocation = ligne.split()
            bareme[float(salaire)] = float(allocation)

    assert mc.caf(0, bareme) == 400.0
    assert mc.caf(500, bareme) == 200.0
    assert mc.caf(1350, bareme) == 150.0
    assert mc.caf(3000, bareme) == 0.0