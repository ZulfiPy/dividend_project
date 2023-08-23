from name_generator import generate_plot_name, df_year
from text_wrapper import wrap_labels
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def percent_formatter(x, pos):
    return f'{x:.0f}%'

def plot_bar_prc(df, x, y, xlabel, ylabel, title, df_name, color='pink'):
    fig_full_name = generate_plot_name(title, df_name) + '.png'
    plot_fin_path = f'/Users/zulf/Documents/GitHub/div/plots/{fig_full_name}'
    new_title = f'{title} ({df_year(df_name)})'

    fig, ax = plt.subplots(figsize=(36, 36))
    ax.bar(df[x], df[y], label=df[x], color=color)
    ax.set_title(new_title, fontsize=32, fontweight='bold')
    ax.set_xlabel(xlabel, fontsize=25, fontweight='bold')
    ax.set_ylabel(ylabel, fontsize=25, fontweight='bold')
    ax.set_xticks(df[x])
    wrap_labels(ax, 10)
    ax.tick_params(axis='y', labelsize=25)
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(percent_formatter))
    ax.grid()

    fig.savefig(plot_fin_path)
    plt.close()


def plot_bar(df, x, y, xlabel, ylabel, title, df_name, color='purple'):
    fig_full_name = generate_plot_name(title, df_name) + '.png'
    plot_fin_path = f'/Users/zulf/Documents/GitHub/div/plots/{fig_full_name}'
    new_title = f'{title} ({df_year(df_name)})'

    fig, ax = plt.subplots(figsize=(36, 46))
    ax.bar(df[x], df[y], label=df[x], color=color)
    ax.set_title(new_title, fontsize=32, fontweight='bold')
    ax.set_xlabel(xlabel, fontsize=25, fontweight='bold')
    ax.set_ylabel(ylabel, fontsize=25, fontweight='bold')
    ax.set_xticks(df[x])
    wrap_labels(ax, 10)
    ax.tick_params(axis='y', labelsize=25)
    ax.grid()

    fig.savefig(plot_fin_path)
    plt.close()