import matplotlib.pyplot as plt


def comparaison_plot_function(score_dict: dict, title=""):
    fig, ax = plt.subplots(figsize=(18, 12))
    shift = 0.2
    data_values = {}
    for index_1, key_1 in enumerate(score_dict.keys()):
        for index_2, key_2 in enumerate(score_dict[key_1].keys()):
            if key_2 not in set(data_values.keys()):
                data_values[key_2] = {"index": [], "values": []}
            data_values[key_2]["index"].append(index_1 + (index_2 - 1) * shift)
            data_values[key_2]["values"].append(score_dict[key_1][key_2])
    for key, value in data_values.items():
        ax.barh(value["index"], value["values"], height=0.2, align="center", label=key)
    ax.invert_yaxis()
    ax.yaxis.set_major_locator(plt.FixedLocator(list(range(3))))
    ax.set_yticklabels(list(score_dict.keys()), fontsize=20)
    ax.tick_params(axis="x", labelsize=20)
    ax.xaxis.grid()
    ax.legend(fontsize=20, ncol=3, loc=(0.25, -0.1))
    ax.set_title(title, fontsize=25)
    plt.show()
