import numpy as np
import matplotlib.pyplot as plt


M = [0, 10]
N = [10, 20]
h1 = [20, 32]
y = [0, 0]
plt.plot(M, y, 'go-', label = 'Duración de las materias')
plt.text(x=5.0, y=0.1, s=u'M = 10', fontsize=10)
plt.plot(N, y, 'go-')
plt.text(x=15.0, y=0.1, s=u'N = 10', fontsize=10)
plt.plot(h1, y, 'ro--')
plt.text(x=25.0, y=0.1, s=u'h1 = 12', fontsize=10)

H = [14, 28]
h2 = [28, 32]
J = [32, 48]
h3 = [48, 50]
y = [1, 1]
plt.plot(H, y, 'go-')
plt.text(x=21.0, y=1.1, s=u'H = 14', fontsize=10)
plt.plot(h2, y, 'ro--')
plt.text(x=29.0, y=1.1, s=u'h2 = 4', fontsize=10)
plt.plot(J, y, 'go-')
plt.text(x=38.0, y=1.1, s=u'J = 16', fontsize=10)
plt.plot(h3, y, 'ro--')
plt.text(x=47.0, y=1.1, s=u'h3 = 2', fontsize=10)

D = [0, 14]
E = [14, 28]
h4 = [28, 32]
y = [2, 2]
plt.plot(D, y, 'go-')
plt.text(x=7.0, y=2.1, s=u'D = 14', fontsize=10)
plt.plot(E, y, 'go-')
plt.text(x=22, y=2.1, s=u'E = 14', fontsize=10)
plt.plot(h4, y, 'ro--', label = 'Tiempo de holgura')
plt.text(x=29, y=2.1, s=u'h4 = 4', fontsize=10)

B = [0, 16]
C = [16, 32]
G = [32, 50]
K = [50, 68]
L = [68, 88]
y = [3, 3]
plt.plot(B, y, 'go-')
plt.text(x=8, y=3.1, s=u'B = 16', fontsize=10)
plt.plot(C, y, 'go-')
plt.text(x=24, y=3.1, s=u'C = 16', fontsize=10)
plt.plot(G, y, 'go-')
plt.text(x=41, y=3.1, s=u'G = 18', fontsize=10)
plt.plot(K, y, 'go-')
plt.text(x=59, y=3.1, s=u'K = 18', fontsize=10)
plt.plot(L, y, 'go-')
plt.text(x=78, y=3.1, s=u'L = 20', fontsize=10)

p1 = [14, 14]
y = [1, 3]
plt.plot(p1, y, 'b--', label = 'Marcas de inicio y fin')

A = [0, 10]
h5 = [10, 16]
F = [16, 32]
y = [4, 4]
plt.plot(A, y, 'go-')
plt.text(x=5, y=4.1, s=u'A = 10', fontsize=10)
plt.plot(h5, y, 'ro--')
plt.text(x=12, y=4.1, s=u'h5 = 6', fontsize=10)
plt.plot(F, y, 'go-')
plt.text(x=24, y=4.1, s=u'F = 16', fontsize=10)

p1 = [16, 16]
y = [3, 4]
plt.plot(p1, y, 'b--')

p1 = [24, 24]
y = [4, 5]
plt.plot(p1, y, 'b--')

p1 = [50, 50]
y = [1, 5]
plt.plot(p1, y, 'b--')


I = [24, 40]
h6 = [40, 50]
y = [5, 5]
plt.plot(I, y, 'go-')
plt.text(x=32, y=5.1, s=u'I = 16', fontsize=10)
plt.plot(h6, y, 'ro--')
plt.text(x=45, y=5.1, s=u'h6 = 10', fontsize=10)

O = [0, 14]
P = [14, 28]
h7 = [28, 88]
y = [6, 6]
plt.plot(O, y, 'go-')
plt.text(x=7, y=6.1, s=u'O = 14', fontsize=10)
plt.plot(P, y, 'go-')
plt.text(x=22, y=6.1, s=u'P = 14', fontsize=10)
plt.plot(h7, y, 'ro--')
plt.text(x=58, y=6.1, s=u'h7 = 60', fontsize=10)

plt.xticks([0,10,20, 30, 40, 50, 60, 70, 80 ,90])
plt.yticks([])
plt.grid()
plt.legend(loc='lower right')
plt.title('Diagrama de barras')
plt.xlabel(u'Duración de las Materias')
plt.ylabel(u'Materias')
plt.show()


