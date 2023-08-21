from generate_final_dfs_for_plot import generate
from text_wraper import wrap_labels
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

#dfs = generate.dfs_for_plot(insert num)

def percent_formatter(x, pos):
    return f'{x:.0f}%'

def plot_bar_prc(df, x, y, xlabel, ylabel, title, color='pink'):
    fig, ax = plt.subplots(figsize=(36, 36))
    ax.bar(df[x], df[y], label=df[x], color=color)
    ax.set_title(title, fontsize=32, fontweight='bold')
    ax.set_xlabel(xlabel, fontsize=25, fontweight='bold')
    ax.set_ylabel(ylabel, fontsize=25, fontweight='bold')
    ax.set_xticks(df[x])
    wrap_labels(ax, 10)
    ax.tick_params(axis='y', labelsize=25)
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(percent_formatter))
    ax.grid()

    #fig.savefig('lol.png')
    plt.show()


def plot_bar(df, x, y, xlabel, ylabel, title, color='purple'):
    fig, ax = plt.subplots(figsize=(36, 46))
    ax.bar(df[x], df[y], label=df[x], color=color)
    ax.set_title(title, fontsize=32, fontweight='bold')
    ax.set_xlabel(title, fontsize=25, fontweight='bold')
    ax.set_ylabel(title, fontsize=25, fontweight='bold')
    ax.set_xticks(df[x])
    wrap_labels(ax, 10)
    ax.tick_params(axis='y', labelsize=25)
    ax.grid()

    # fig.savefig('lol.png')
    plt.show()

