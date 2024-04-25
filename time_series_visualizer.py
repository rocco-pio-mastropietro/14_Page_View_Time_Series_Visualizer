import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Clean data
df = df.loc[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    df_line = df.copy()
    x = df_line.index
    y = df_line['value']
    
    fig, ax = plt.subplots(figsize=(9.6, 7.2))
    
    ax.plot(x, y, 'tab:red')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set(xlabel='Date', ylabel='Page Views')
            
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['years'] = [y.year for y in df_bar.index]
    df_bar['month_numbers'] = [m.month for m in df_bar.index]
    df_bar['months'] = [m.strftime('%B') for m in df_bar.index]
    df_bar = df_bar[['years', 'month_numbers', 'months', 'value']]    
    df_bar.sort_values('month_numbers', inplace=True)
    
    # Draw bar plot
    fig, ax = plt.subplots(figsize=(9.6, 7.2))
    
    ax = sns.barplot(data=df_bar, x='years', y='value', hue='months', errorbar=None, palette=sns.color_palette())
    sns.move_legend(ax, 'upper left')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.xticks(rotation=90)
    
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
