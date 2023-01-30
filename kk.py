import pandas as pd
import numpy as np
from numpy import NaN
from sklearn import preprocessing

df = pd.DataFrame({'bust': [99, 89, 91, 91, 86, 97, NaN],
                   'waidt': [56, 58, 64, 51, 56, 53, 51],
                   'hips': [91, 89, 91, 91, 84, 86, 91],
                   'height': [160, 157, 165, 170, 157, 175, 165],
                   'weight': [58, 48, 54, 54, 44, 56, 54]}, index=['W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7'])


def pred_kk_by_feature(df, pred_object, pred_feature):
    temp = df.corr()[pred_feature]
    KK = temp[temp.index != pred_feature]
    KK  # КК для всех признаков

    temp = df[df.index != pred_object].mean(axis=0)
    mean_all_feature = temp[temp.index != pred_feature]
    mean_all_feature  # Среднее значение для всех признаков (кроме предсказываемого) по всем наблюдениям (кроме предсказываемого)

    all_feature_pred_object = df.loc[pred_object][
        df.loc[pred_object].index != pred_feature]  # Значения известных признаков предсказываемого наблюдения
    dif_mult_kk = ((
                               all_feature_pred_object - mean_all_feature) * KK).sum()  # сумма произведений разности известных значений и средних, и КК
    mean_feature_pred_object = df[pred_feature].mean()  # среднее значение признака
    pred_feature_object = mean_feature_pred_object + 1 / KK.abs().sum() * dif_mult_kk  # получаем предсказание пропущенного значения

    print(f'Значение признака, рассчитанное с помощью КК (по признакам) : {round(pred_feature_object, 2)}')
    return (pred_feature_object)


def pred_kk_by_object(df, pred_object, pred_feature):
    temp = df.transpose().corr()[pred_object]  # транспонируем данные для рассчета КК между объектами
    KK = temp[temp.index != pred_object]

    temp = df.transpose()[df.transpose().index != pred_feature].mean(
        axis=0)  # среднее значение всех признаков (кроме предсказываемого) в известных объектах
    mean_all_object = temp[temp.index != pred_object]

    all_object_pred_feature = df.transpose().loc[pred_feature][df.transpose().loc[
                                                                   pred_feature].index != pred_object]  # значения предсказываемого признака для известных объектов
    dif_mult_kk = ((
                               all_object_pred_feature - mean_all_object) * KK).sum()  # сумма произведений разности известных значений и средних, и КК
    norm_mult = 1 / KK.abs().sum()  # нормирующий множитель
    mean_W = df.mean(axis=1)[pred_object]  # среднее значение всех признаков для W7

    pred_feature_object = mean_W + norm_mult * dif_mult_kk  # получаем предсказание пропущенного значения

    print(f'Значение признака, рассчитанное с помощью КК (по объектам) : {round(pred_feature_object, 2)}')
    return (pred_feature_object)


def pred_metric(metric_name, df, pred_object, pred_feature):
    min_max_scaler = preprocessing.MinMaxScaler()  # создаем объект нормализации
    # затем вызываем метод fit_transform, передаем в него датафрейм с нужными колонками (преобразованный в массив),
    # полученный массив преобразуем обратно в датафрейм и присваиваем его значению изначальных колок
    df[df.columns[df.columns != pred_feature]] = pd.DataFrame(
        min_max_scaler.fit_transform(df.transpose()[df.transpose().index != pred_feature].transpose().values),
        columns=df.columns[df.columns != pred_feature], index=df.index)

    temp = df.transpose()[pred_object]
    feature_pred_object = temp[temp.index != pred_feature]  # признаки для предсказываемого объекта

    dict_metric = {}  # создаем словарь метрик, преобразуем его в датафрейм
    for name_object in df.index[df.index != pred_object]:
        t = df.loc[name_object]
        if metric_name == 'euclid':
            dict_metric[name_object] = np.power((feature_pred_object - t[t.index != pred_feature]).pow(2).sum(),
                                                0.5).round(2)
        elif metric_name == 'manhatten':
            dict_metric[name_object] = (feature_pred_object - t[t.index != pred_feature]).abs().sum()
        else:
            dict_metric[name_object] = (feature_pred_object - t[t.index != pred_feature]).abs().max()
    metric = pd.DataFrame(data=dict_metric, index=[metric_name]).transpose()

    temp = df.transpose()[df.transpose().index == pred_feature].transpose()
    feature_other_objects = temp[temp.index != pred_object]  # предсказываемый признак для других объектов

    norm_mul = 1 / ((1 / metric).sum()).item()  # нормирующий множитель
    similarity = (
                feature_other_objects.values / metric.values).sum()  # значение признака * мера близости(=величина, обратно пропорциональная мере расстояния)
    pred_feature_object = norm_mul * similarity
    print(f'Значение признака, рассчитанное по метрике {metric_name}: {round(pred_feature_object, 2)}')
    return pred_feature_object


pred_object = 'W7'
pred_feature = 'bust'

methods = {'pred_kk_by_feature': pred_kk_by_feature(df, pred_object, pred_feature),
           'pred_kk_by_object': pred_kk_by_object(df, pred_object, pred_feature),
           'pred_metric_euclid': pred_metric('euclid', df, pred_object, pred_feature),
           'pred_metric_manhatten': pred_metric('manhatten', df, pred_object, pred_feature),
           'pred_metric_max_metric': pred_metric('max_metric', df, pred_object, pred_feature)}

for method in methods.values():
    method