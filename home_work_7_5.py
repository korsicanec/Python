# Користувач робить внесок в розмірі n гривень строком на years років під 10% річних (щороку розмір його внеску збільшується на 10%. 
# Ці гроші додаються до суми вкладу, і на них в наступному році теж будуть відсотки).

def bank(a, years):
    for year in range(years):
        a *= 1.1
    return a
