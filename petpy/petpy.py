"""
petrophysics equations
"""
def gardner(vp,alpha=310,beta=0.25):
    return alpha*vp*beta


def impedance(vp,rho):
    """
    This function calculates an impedance value
    """
    ai = vp*rho
    return ai

