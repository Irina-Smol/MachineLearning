# Matplotlib

## lesson 1

Компоненты графика:

![1](https://sun9-east.userapi.com/sun9-35/s/v1/ig2/R3NOpuetnNcBDIswgPuCoqT5iqWKxdel8FJsiktRoXGc-6SRDUjMDxbia3SbybPM6TR4YkB4gYbSVCB9XjItUs48.jpg?size=638x377&quality=96&type=album)

![2](https://sun9-west.userapi.com/sun9-13/s/v1/ig2/lqVmM2Mg_8TEHwlEPMAySM0gWR0CTp9vV2thegCCBdh-gu7fDmMIWDXQebcelnFvqY6wLyFGZcMXxIZl7qFNxks2.jpg?size=605x299&quality=96&type=album)

В основе всего лежит фигура (Figure) и она одна для текущего окна. 
Затем, на фигуре располагаются координатные оси (Axes). Таких осей (объектов Axes) может совсем не быть, но, как правило, имеется хотя бы одна область.
Каждый объект Axes содержит две или три координатные оси (Axis), сетку, метки (ticks), легенду и, конечно же, графики. 
Причем число графиков может быть произвольным – от нуля и до любого разумного числа.

Объект Artist отвечает за размещение и оформление отображаемых данных на рисунке (Figure) и взаимодействует непосредственно с объектом 
Canvas – подложки для рисования на холсте (рисунке).

Оси Axis в matplotlib могут иметь разные конфигурации:

- в виде декартовой системы на плоскости (2D) или в пространстве (3D);
- использовать логарифмический масштаб по каждой из осей;
- описывать сферическую систему координат.
