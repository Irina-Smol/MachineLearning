# логарифмический масштаб у координатных осей

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()

x = np.arange(-10 * np.pi, 10 * np.pi, 0.5)
ax.plot(x, np.sinc(x) * np.exp(-np.abs(x / 10)))
ax.grid()

plt.show()

# здесь может помочь логарифмический масштаб по оси ординат. Для этого достаточно воспользоваться методом semilogy(),
# чтобы по оси Oy откладывался логарифмический масштаб (логарифм по основанию 10)

# 2
fig1 = plt.figure(figsize=(7, 4))
ax1 = fig1.add_subplot()

x1 = np.arange(-10 * np.pi, 10 * np.pi, 0.5)
ax1.semilogy(x, np.sinc(x) * np.exp( -np.abs(x/10)) )
ax1.grid()

plt.show()

# 3
fig2 = plt.figure(figsize=(7, 4))
ax2 = fig2.add_subplot()

x2 = np.arange(-10 * np.pi, 10 * np.pi, 0.5)
# Того же самого эффекта можно добиться и с помощью прежней функции plot(), только дополнительно указать логарифмический масштаб по нужной оси
ax2.plot(x, np.sinc(x) * np.exp( -np.abs(x/10)) )
ax2.set_yscale('log')

ax2.grid()

plt.show()

# здесь можно использовать три разных масштаба:

# 'linear' – линейный масштаб (используется по умолчанию);
# 'log' – логарифмический масштаб;
# 'symlog' – вблизи нуля (в указанных пределах) масштаб линейный, а в остальной области – логарифмический.

# Как я только что отмечал, логарифмический масштаб формируется по основанию 10. Если нужно изменить и указать другое основание, то это делается с помощью параметра base:
# ax.set_yscale('log', base=5)

# 4 по вертикали дополнительно отложены небольшие риски. Мы можем управлять их отображением, указав их значения в виде целых чисел в списке параметра subs

fig3 = plt.figure(figsize=(7, 4))
ax3 = fig3.add_subplot()

x3 = np.arange(-10 * np.pi, 10 * np.pi, 0.5)
ax3.plot(x, np.sinc(x) * np.exp( -np.abs(x/10)) )
ax3.set_yscale('log', subs=[2, 9])
ax3.grid()

plt.show() # мы указываем отображать риску со значением 0,2 или 0,02 или 0,002 и т.д. И риску со значениями 0,9 или 0,09 или 0,009 и т.д

# 5 возможность использования третьего параметра 'symlog'
fig4 = plt.figure(figsize=(7, 4))
ax4 = fig4.add_subplot()

x4 = np.arange(-10 * np.pi, 10 * np.pi, 0.5)
ax4.plot(x, np.sinc(x) * np.exp( -np.abs(x/10)) ) # использован дополнительный параметр linthresh, определяющий
                                                  # граничное значение [-2; 2], где график следует отображать в линейном масштабе.
                                                  # А все, что выходит за эти пределы – в логарифмическом
ax4.set_xscale('symlog', linthresh=2)
ax4.grid()

plt.show()

# 6 Дополнительно линейный масштаб можно растянуть, указав масштаб в дополнительном параметре linscale

fig5 = plt.figure(figsize=(7, 4))
ax5 = fig5.add_subplot()

x5 = np.arange(-10 * np.pi, 10 * np.pi, 0.5)
ax5.plot(x, np.sinc(x) * np.exp( -np.abs(x/10)))
ax5.set_xscale('symlog', linthresh=2, linscale=5)
ax5.grid()

plt.show()

# 7 если нам нужно установить логарифмический масштаб по обеим осям, то проще всего для этого воспользоваться функцией loglog(),
# вместо функции plot() или semilogx()/semilogy()

fig6 = plt.figure(figsize=(7, 4))
ax6 = fig6.add_subplot()

x6 = np.arange(-10 * np.pi, 10 * np.pi, 0.5)
ax6.loglog(x, np.sinc(x) * np.exp( -np.abs(x/10)) )
ax6.grid()

plt.show()




