# Genus of Y^2 = Q(x,1) for each of Bremner II's three (13) quartics at lambda=13.
# Each Q is a homogeneous quartic in (p,q); set x=p/q and take the affine model Y^2=f(x).
from sage.all import *

quartics = {
 'Q1a': 4*(9409*x**4 + 1352*x**3 + 1346*x**2 - 1352*x + 9409),
 'Q1b': 4*(5041*x**4 - 30252*x**3 + 27554*x**2 + 30252*x + 5041),
 'Q1c': 4*(9409*x**4 + 30252*x**3 + 1346*x**2 - 30252*x + 9409),
}

x = var('x')
for name, f in quartics.items():
    fpoly = QQ['x'](f)
    # squarefree?
    print(name, "leading coeff", fpoly.leading_coefficient())
    # smooth projective curve X: v^2 = w^4 f(w?) ... put x=X/Z, y=Y/Z^2:
    # use Sage's genus on HyperellipticCurve with odd/even degree.
    R = PolynomialRing(QQ, 'x')
    ff = R(fpoly)
    # Curve y^2 = f(x), f degree 4: HyperellipticCurve handles even degree -> genus 2? 
    H = HyperellipticCurve(ff)
    print("   HyperellipticCurve genus:", H.genus())
    # Also check the squarefree-ness of f and of the "points at infinity" structure.
    print("   f squarefree:", ff.is_squarefree())
    # Distinct roots count over QQbar
    nroots = len(ff.roots(QQbar, multiplicities=False))
    print("   distinct roots over QQbar:", nroots)
