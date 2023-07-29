import pandas as pd 
import matplotlib.pyplot as plt

# Путь к сохранению картинок
path_save = 'D:\\Работа\\Тестовые задания\\Вакансия Junior Data Analyst НИУ ВШЭ\\картинки\\'

# Загрузка таблицы csv
data = pd.read_csv('Тестовое задание_formatted.csv', decimal=',')

# Настройка типов данных
data['cluster'] = data['cluster'].astype (int)
data['count'] = data['count'].astype (int)
data['x'] = data['x'].astype (float)
data['y'] = data['y'].astype (float)
data.dtypes

# Получение списка всех неповторяющихся area
data_group = data.groupby('area').count()
data_group = data_group.reset_index()
data_group_list = data_group.iloc[:,0].to_list()

# Создание картинок + их сохранение
for name_area in data_group_list:
    
    # name_area = data_group_list[14]
    # print(name_area)

    # Загрузка данных из одной области (area)
    data_single_area = data.loc[data['area'] == name_area, :]
    data_single_area = data_single_area.reset_index(drop=True)
    
    # Настройка размера картинки
    plt.figure(figsize=(20, 20), dpi = 200)

    #hide axes and borders
    plt.axis('off')
    
    # Расставляем точки
    for n_cluster in range(4):
        data_single_cluster = data_single_area.loc[data_single_area['cluster'] == n_cluster, :]
        data_single_cluster = data_single_cluster.reset_index(drop=True)
        plt.scatter(data_single_cluster.loc[:, 'x'], data_single_cluster.loc[:, 'y'], s=200, color=data_single_cluster.loc[0, 'color'], edgecolors='black', label=data_single_cluster.loc[0, 'cluster_name'])
    
    # Расставляем текст к точкам
    for i in range(len(data_single_area)):
        # делим текст на слова, разделяя по строкам каждое слово
        if len(data_single_area.loc[i, 'keyword']) > 15:
            words = data_single_area.loc[i, 'keyword'].split()
            con_keyword = '\n'.join(words)
        
        plt.text(data_single_area.loc[i, 'x'] - 0.5, data_single_area.loc[i, 'y'] + 0.2, con_keyword, fontsize=15)

    # добавляем легенду
    plt.legend(title='Кластеры', fontsize=15, title_fontsize=18, loc=7)
    
    # сохранение в .png формате
    if data_single_area.loc[0, 'area'] == 'ar\\vr':
        plt.savefig(path_save + 'arvr.png')
    else:
        plt.savefig(path_save + '{}.png'.format(data_single_area.loc[0, 'area']))
    
    # показываем картинку в программе
    plt.show()

    
   