import numpy as np
import matplotlib.pyplot as plt


def distribucionGeometrica(n):
  z = np.random.geometric(p=0.2, size=n)
  #print((z == 1).sum() / n)
  return z
def distribucionExponencial(n):
  z = np.random.exponential(scale=1.0,  size=n)
  return z
def distribucionCauchy(n):
  z = np.random.standard_cauchy(n)
  return z
def plot(datos, epsilon = None  , name = "grafica.png"):
  fig, ax = plt.subplots()
  ax.plot( datos )
  if epsilon != None:
    ax.plot( epsilon )
  ax.grid()
  fig.savefig(name)

def histograma(datos, name="histograma.png"):
  fig, ax = plt.subplots()
  #ax.plot( datos )
  #ax.plot( auxl )
  ax.hist(datos, bins = 60)

  ax.grid()
  fig.savefig(name)