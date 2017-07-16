from PhyPraKit import *
import matplotlib.pyplot as plt
picoscopefile = '../Daten/Frank_Hertz_2.psdata'
savefile = '../Daten/Frank_Hertz_2_py.pdf'
data = readPicoScope(picoscopefile)
plt.plot(data)
plt.savefig(savefile)
plt.show()
