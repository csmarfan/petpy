"""
petrophysics equations
"""
def gardner(vp,alpha=310,beta=0.25):
    return alpha*vp*beta

def impedance(vp,rho1):
    ai = vp*rho1
    return ai

