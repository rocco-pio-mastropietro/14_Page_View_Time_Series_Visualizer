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
    
    fig, ax = plt.subplots(figsize = [12.8, 7.2])

    ax.plot(x, y, 'tab:red')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set(xlabel='Date', ylabel='Page Views')
            
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar = df_bar.reset_index()
    df_bar['year'] = df_bar['date'].dt.year
    df_bar['month'] = df_bar['date'].dt.month
    df_bar['month_name'] = df_bar['date'].dt.month_name()
    df_bar = df_bar.groupby(by=['year', 'month'])[['value']].mean().unstack()

    # Draw bar plot
    fig, ax = plt.subplots(figsize = [9.6, 7.2])

    df_bar.plot(kind='bar', ax=ax)

    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], title='Months', loc='upper left')
    
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]   
    df_box['month_numbers'] = [m.month for m in df_box.date]
    df_box.sort_values('month_numbers', inplace=True)

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize = [12.8, 6.4])

    sns.boxplot(data=df_box, x='year', y='value', orient='v', palette=sns.color_palette(), ax=ax1)
    sns.boxplot(data=df_box, x='month', y='value', orient='v', ax=ax2)
    
    ax1.set_ylim(0, 200000)
    ax1.locator_params(axis='y', nbins=10)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set(xlabel='Year', ylabel='Page Views')
    
    ax2.set_ylim(0, 200000)
    ax2.locator_params(axis='y', nbins=10)
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set(xlabel='Month', ylabel='Page Views')
    
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
