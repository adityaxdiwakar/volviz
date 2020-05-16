import os

vix_data_dir = "bin/vix_data/"

files = [file for file in os.listdir(vix_data_dir) if file.endswith(".json")]
files = sorted(files, key=lambda file: file[0])

mdp = {}
date_dict = {}
for fn in files:
    with open(vix_data_dir + fn, "r") as f:
        file = f.readlines()
       
    file = [line.replace("\n", "").split(",") for line in file]

    dp = {}
    for line in file:
        if line[1] not in date_dict:
            if len(date_dict) == 0:
                date_dict.update({line[1]: 0})
            else:
                date_dict.update({line[1]: max(list(date_dict.values())) + 1})
        di = date_dict[line[1]]

        dp.update({di: float(line[2])})

    mdp.update({fn[2:-5]: dp})

import plotly.graph_objects as go

max_len = max([len(values) for month, values in mdp.items()])

z = []
for i in range(100, max_len):
    arr = []
    for month in mdp:
        if i in mdp[month]:
            arr.append(mdp[month][i])
    z.append(arr)
z.reverse()

string = ""
for x in z:
    for y in x:
        string += str(y) + ","
    string += "\n"

with open("bin/dump.csv", "w") as f:
    f.write(string)

import pandas as pd

data = pd.read_csv("bin/dump.csv")

fig = go.Figure(data=go.Surface(x=list(range(7)), y=list(range(max_len)), z=data.values))
                
fig.update_layout(title='Volatility Index', autosize=False,
                  width=1250, height=1000, template="plotly_dark", margin=dict(l=65, r=50, b=65, t=90))

fig.show()