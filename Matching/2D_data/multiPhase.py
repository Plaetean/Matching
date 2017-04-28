import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pickle
import numpy as np

fname="phase_s20psi1"
fname2="phase_s20psi4"

#Data saved in the form of x values, y values, z values
x,y,z,specs=pickle.load(open("%s.p" % fname,"rb"))
x2,y,z,specs=pickle.load(open("%s.p" % fname,"rb"))
m1=specs[0]
m2=specs[1]

plt.figure()
plt.subplot(2,2,1)
plt.contourf(x,y,z,200,cmap="inferno")
plt.colorbar()
plt.subplot(2,2,2)
plt.contourf(x2,y,z,200,cmap="inferno")
plt.colorbar()
plt.subplot(2,2,3)
plt.contourf(x2,y,z,200,cmap="inferno")
plt.colorbar()
plt.subplot(2,2,4)
plt.contourf(x2,y,z,200,cmap="inferno")
plt.colorbar()
plt.ylabel("phase")
plt.xlabel("inclination")
plt.title("m1=%s, approx=%s" % (m1,specs[2]))
plt.show("hold")
plt.savefig("multi.png")
print "DONE"
