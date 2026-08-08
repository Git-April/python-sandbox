from scipy import constants #SciPy Home
import scipy #SciPy Getting Started
from scipy.optimize import minimize
import numpy as np #SciPy Sparse Data
from scipy.sparse import csr_matrix #SciPy Sparse Data
from scipy.sparse.csgraph import connected_components, dijkstra, floyd_warshall, bellman_ford, depth_first_order, breadth_first_order #SciPy Graphs
from scipy.spatial import Delaunay, ConvexHull, KDTree #SciPy Spatial Data
import matplotlib.pyplot as plt #SciPy Spatial Data
from scipy.spatial.distance import euclidean, cityblock, cosine, hamming #SciPy Spatial Data
from scipy import io #SciPy Matlab Arrays
from scipy.interpolate import interp1d, UnivariateSpline, Rbf #SciPy Interpolation
from scipy.stats import ttest_ind, kstest, describe, skew, kurtosis, normaltest #SciPy Significance Tests

#SciPy Home
print(constants.liter)

#SciPy Getting Started
print(constants.liter)

print(scipy.__version__)

#SciPy Constants
print(constants.pi)

print(dir(constants))

print(constants.yotta)
print(constants.zetta)
print(constants.exa)
print(constants.peta)
print(constants.tera)
print(constants.giga)
print(constants.mega)
print(constants.kilo)
print(constants.hecto)
print(constants.deka)
print(constants.deci)
print(constants.centi)
print(constants.milli)
print(constants.micro)
print(constants.nano)
print(constants.pico)
print(constants.femto)
print(constants.atto)
print(constants.zepto)

print(constants.kibi)
print(constants.mebi)
print(constants.gibi)
print(constants.tebi)
print(constants.pebi)
print(constants.exbi)
print(constants.zebi)
print(constants.yobi)

print(constants.gram)
print(constants.metric_ton)
print(constants.grain)
print(constants.lb)
print(constants.pound)
print(constants.oz)
print(constants.ounce)
print(constants.stone)
print(constants.long_ton)
print(constants.short_ton)
print(constants.troy_ounce)
print(constants.troy_pound)
print(constants.carat)
print(constants.atomic_mass)
print(constants.m_u)
print(constants.u)

print(constants.degree)
print(constants.arcmin)
print(constants.arcminute)
print(constants.arcsec)
print(constants.arcsecond)

print(constants.minute)
print(constants.hour)
print(constants.day)
print(constants.week)
print(constants.year)
print(constants.Julian_year)

print(constants.inch)
print(constants.foot)
print(constants.yard)
print(constants.mile)
print(constants.mil)
print(constants.pt)
print(constants.point)
print(constants.survey_foot)
print(constants.survey_mile)
print(constants.nautical_mile)
print(constants.fermi)
print(constants.angstrom)
print(constants.micron)
print(constants.au)
print(constants.astronomical_unit)
print(constants.light_year)
print(constants.parsec)

print(constants.atm)
print(constants.atmosphere)
print(constants.bar)
print(constants.torr)
print(constants.mmHg)
print(constants.psi)

print(constants.hectare)
print(constants.acre)

print(constants.liter)
print(constants.litre)
print(constants.gallon)
print(constants.gallon_US)
print(constants.gallon_imp)
print(constants.fluid_ounce)
print(constants.fluid_ounce_US)
print(constants.fluid_ounce_imp)
print(constants.barrel)
print(constants.bbl)

print(constants.kmh)
print(constants.mph)
print(constants.mach)
print(constants.speed_of_sound)
print(constants.knot)

print(constants.zero_Celsius)
print(constants.degree_Fahrenheit)

print(constants.eV)
print(constants.electron_volt)
print(constants.calorie)
print(constants.calorie_th)
print(constants.calorie_IT)
print(constants.erg)
print(constants.Btu)
print(constants.Btu_IT)
print(constants.Btu_th)
print(constants.ton_TNT)

print(constants.hp)
print(constants.horsepower)

print(constants.dyn)
print(constants.dyne)
print(constants.lbf)
print(constants.pound_force)
print(constants.kgf)
print(constants.kilogram_force)

#SciPy Optimizers
def eqn(x):
  return x**2 + x + 2
mymin = minimize(eqn, 0, method='BFGS')
print(mymin)

#SciPy Sparse Data
arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])
print(csr_matrix(arr))

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
print(csr_matrix(arr).data)

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
print(csr_matrix(arr).count_nonzero())

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
mat = csr_matrix(arr)
mat.eliminate_zeros()
print(mat)

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
mat = csr_matrix(arr)
mat.sum_duplicates()
print(mat)

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
newarr = csr_matrix(arr).tocsc()
print(newarr)

#SciPy Graphs
arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])
newarr = csr_matrix(arr)
print(connected_components(arr))

arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])
newarr = csr_matrix(arr)
print(dijkstra(newarr, return_predecessors=True, indices=0))

arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])
newarr = csr_matrix(arr)
print(floyd_warshall(newarr, return_predecessors=True))

arr = np.array([
  [0, -1, 2],
  [1, 0, 0],
  [2, 0, 0]
])
newarr = csr_matrix(arr)
print(bellman_ford(newarr, return_predecessors=True, indices=0))

arr = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])
newarr = csr_matrix(arr)
print(depth_first_order(newarr, 1))

arr = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])
newarr = csr_matrix(arr)
print(breadth_first_order(newarr, 1))

#SciPy Spatial Data
points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1]
])
simplices = Delaunay(points).simplices
# plt.triplot(points[:, 0], points[:, 1], simplices)
# plt.scatter(points[:, 0], points[:, 1], color='r')
# plt.show()

points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1],
  [1, 2],
  [5, 0],
  [3, 1],
  [1, 2],
  [0, 2]
])
hull = ConvexHull(points)
hull_points = hull.simplices
plt.scatter(points[:, 0], points[:, 1])
# for simplex in hull_points:
#   plt.plot(points[simplex,0], points[simplex,1], 'k-')
# plt.show()

points = [(1, -1), (2, 3), (-2, 3), (2, -3)]
kdtree = KDTree(points)
res = kdtree.query((1, 1))
print(res)

p1 = (1, 0)
p2 = (10, 2)
res = euclidean(p1, p2)
print(res)

p1 = (1, 0)
p2 = (10, 2)
res = cityblock(p1, p2)
print(res)

p1 = (1, 0)
p2 = (10, 2)
res = cosine(p1, p2)
print(res)

p1 = (True, False, True)
p2 = (False, True, True)
res = hamming(p1, p2)
print(res)

#SciPy Matlab Arrays
arr = np.arange(10)
io.savemat('arr.mat', {"vec":arr})

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
io.savemat('arr.mat', {"vec": arr})
mydata = io.loadmat('arr.mat')
print(mydata)
print(mydata['vec'])
mydata = io.loadmat('arr.mat', squeeze_me=True)
print(mydata['vec'])

#SciPy Interpolation
xs = np.arange(10)
ys = 2*xs + 1
interp_func = interp1d(xs, ys)
newarr = interp_func(np.arange(2.1, 3, 0.1))
print(newarr)

xs = np.arange(10)
ys = xs**2 + np.sin(xs) + 1
interp_func = UnivariateSpline(xs, ys)
newarr = interp_func(np.arange(2.1, 3, 0.1))
print(newarr)

xs = np.arange(10)
ys = xs**2 + np.sin(xs) + 1
interp_func = Rbf(xs, ys)
newarr = interp_func(np.arange(2.1, 3, 0.1))
print(newarr)

#SciPy Significance Tests
v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)
res = ttest_ind(v1, v2)
print(res)
res = ttest_ind(v1, v2).pvalue
print(res)

v = np.random.normal(size=100)
res = kstest(v, 'norm')
print(res)

v = np.random.normal(size=100)
res = describe(v)
print(res)

v = np.random.normal(size=100)
print(skew(v))
print(kurtosis(v))

v = np.random.normal(size=100)
print(normaltest(v))