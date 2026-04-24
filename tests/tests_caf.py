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