import matplotlib.pyplot as plt
import json
from datetime import datetime

def get_data_plot():
    with open('market-price.json') as file:
        data = json.load(file)
        return data
    
def data_plot():
    data = get_data_plot()
    x_list = []
    y_list = []
    for item in data["market-price"]:
        x_list.append(item["x"])
        y_list.append(item['y'])
    return x_list, y_list

plt.title('График рыночной стоимости', fontsize = 22, fontweight='bold', color='blue')
plt.xlabel('Период', fontsize = 18, color='black')
plt.ylabel('Рыночная стоимость', fontsize = 16, color='black')
plt.plot(*data_plot(), label='Рыночная стоимость')
plt.legend()
plt.grid()
plt.show()