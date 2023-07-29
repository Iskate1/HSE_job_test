import pandas as pd 
# import numpy as np

# ввод исходной csv таблицы
data = pd.read_csv('Тестовое задание - tz_data.csv', decimal=';')

# =============================================================================
# Форматирование
# удаление колонки good(1), отвечающей за заливку 
data.drop(data.columns[4], axis=1, inplace=True)

# удаление строк
# все значения пустые (nan): 193
# в столбце count пустыме\неформатные значения: 217, 49, 178
# в столбце x пустыме\неформатные значения: 
# в столбце y пустыме\неформатные значения: 99 
data.drop(labels = [49, 99, 178, 193, 217], axis=0, inplace=True)

# изменение типа данных в столбце
data.dtypes
data['cluster'] = data['cluster'].astype (int)
data['count'] = data['count'].astype (int)
data['x'] = data['x'].astype (float)
data['y'] = data['y'].astype (float)
data.dtypes

# сбросить индексы
data = data.reset_index(drop=True)

# =============================================================================
# ПУНКТ 2

# обозначение цветов для кластеров (одинаковых)
colors_cluster = {0 : 'red', 1 : 'green', 2 : 'blue', 3 : 'yellow'}

# создание столбца color и обозначение цветом
data['color'] = 0 
for i in range (len(data)):
    data.loc[i, 'color'] = colors_cluster[data.loc[i, 'cluster']]
    
# =============================================================================
# ПУНКТ 3
 
# Получение списка всех неповторяющихся area
data_group = data.groupby('area').count()
data_group = data_group.reset_index()
data_group_list = data_group.iloc[:,0].to_list()


# Удаляем дубликаты keyword, лежащих в одной области(area)
data_all = pd.DataFrame()
for name_area in data_group_list:
    data_dubl = data.loc[data['area'] == name_area, :].drop_duplicates(subset=['keyword'])
    data_all = pd.concat([data_all, data_dubl])

# data_all_group = data_all.groupby('area').count()
# Удалено дублирующих строк 7:
# ar/vr 1
# dialog 1
# eligibility 2
# greeting 1
# twisted 2

# =============================================================================
# ПУНКТ 4

# Меняем расстановку строк, как в пункте 1
data_all = data_all[['area', 'cluster', 'cluster_name', 'keyword', 'x', 'y', 'count', 'color']]

# Сортируем столбцы 'area', 'cluster', 'count' 
# сортировка столбца 'cluster_name' не требуется, так как номер кластера включен в название
data_all = data_all.sort_values(['area', 'cluster', 'count'], ascending = ( True , True, False ))

# =============================================================================
data_all.to_csv('Тестовое задание_formatted.csv', encoding = 'utf-8', index= False )

# data = pd.read_csv('Тестовое задание_formatted.csv', decimal=',')