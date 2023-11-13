import matplotlib
import matplotlib.pyplot as plt

print(matplotlib.get_backend()) # импортировали модуль matplotlib и вызвали функцию get_backend() для
                                # получения информации о текущем выбранном backend’е. У меня в консоли выводится строка:
                                # TkAgg
# matplotlib.use('Qt5Agg')
'''
поддерживаются следующие backend’ы:

Qt5Agg - Рендеринг графики в Qt5 (требуется PyQt5). В IPython активируется командой %matplotlib qt5
ipympl - Рендеринг графики в виджете Jupyter (требуется ipympl). В IPython активируется командой %matplotlib ipympl
GTK3Agg - Рендеринг графики в GTK 3.x (требуется PyGObject и pycairo или cairocffi). В IPython активируется командой %matplotlib gtk3
macosx - Рендеринг графики в Cocoa. В IPython активируется командой %matplotlib osx
TkAgg - Рендеринг графики в Tk (требуется TkInter). В IPython активируется командой %matplotlib tk
nbAgg- Рендеринг графики в Jupyter notebook. В Jupyter активируется командой %matplotlib notebook
WebAgg - Для использования с торнадо-сервером.
GTK3Cairo - Cairo рендеринг графики в GTK 3.x x (требуется PyGObject и pycairo или cairocffi).
Qt4Agg - Рендеринг графики в Qt4 (требуется PyQt4 или pyside). В IPython активируется командой %matplotlib qt4
wxAgg - Рендеринг графики в wxWidgets (требуется wxPython 4). В IPython активируется командой %matplotlib wx
'''

plt.plot([1, 2, -6, 0, 4]) # отображениe простейшей кривой
plt.grid()
plt.show()
