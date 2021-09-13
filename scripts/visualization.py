import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.gridspec as gridspec
import math

sns.set_theme(style="whitegrid")
sns.set(rc={'figure.figsize':(480/96, 480/96)})

def get_rows_cols_for_subplot(num_subplots:int)->tuple:
    """
    This function calculates the rows and cols required
    for the subplot..
    
    Args:
        num_subplots:int
    
    Returns:
        nrows:int
        ncols:int
        odd:bool
    """
    
    try:
        nrows=ncols=0
        odd=False
        
        if num_subplots%2==0 and num_subplots!=2:
            nrows=ncols=round(num_subplots/2)
        elif num_subplots==2:
            nrows=1
            ncols=2
        else:
            nrows=ncols=math.ceil(num_subplots/2)
            odd=True
            
        return nrows,ncols,odd
    except Exception as error:
        raise Exception('Caught this error: ' + repr(error))

def get_axes_object_for_subplots(nrows:int,
                                 ncols:int,
                                 odd:bool,
                                 fig ,
                                 sharey:bool=True,)->list:
    """
    This function creates the axes object used for subplot
    and retunrs the axes list.
    
    Args:
        nrows:int
        ncols:int
        odd:bool
        fig:matplotlib.figure.Figure
        sharey:bool

    Returns:
        axes_list-> list
    """
    try:

        # Create nxn sub plots
        gs = gridspec.GridSpec(nrows, ncols)

        axes_list = []
        
        for i in range(nrows):
            for j in range(ncols):
                
                if odd:
                    
                    if j==1:
                        odd=False
                        continue
                    else:
                        axes_list.append(fig.add_subplot(gs[i,:]))
                        
                else:
                    
                    if j==1:
                        if sharey:
                            axes_list.append(fig.add_subplot(gs[i,j], sharey = axes_list[-1]))
                        else:
                            axes_list.append(fig.add_subplot(gs[i,j]))
                    else:
                        axes_list.append(fig.add_subplot(gs[i,j]))
                        
        return axes_list

    except Exception as error:
        raise Exception('Caught this error: ' + repr(error))

def create_several_barplots_in_a_figure(data:pd.core.frame.DataFrame,
                                        x_axis_col_names:list,
                                        y_axis_col_names:list,
                                        hue_col_names:list,
                                        num_subplots:int=3,
                                        figure_title:str ='Monthly Gross margin(%) by products and providers',
                                        fontsize:int=16,
                                        save_file:str='barplot.png',
                                        sort:bool=False,
                                        sharey:bool=True,
                                        save_path:str = None)->None:
    """
    This function creates and plots several barplots in a figure.
    
    Args:
        data:pd.core.frame.DataFrame 
        x_axis_col_names:list        -> chronological list of dataframe column names for x axis
        y_axis_col_names:list        -> chronological list of dataframe column names for y axis
        hue_col_names:list           -> chronological list of dataframe column names for hue
        num_subplots:int
        figure_title:str
        fontsize:int
        sharey:bool                  -> wheather to sharen y-axis in same row
        save_path:str
    
    """
    
    try:
        if num_subplots<2:
            raise ValueError("Inadequate number of subplots.")
        elif num_subplots>4:
            raise ValueError("Not Implemented Error!")
            
        elif num_subplots!=len(x_axis_col_names) or \
           num_subplots!=len(y_axis_col_names) or \
           num_subplots!=len(hue_col_names):
            
            raise ValueError("Inadequate input for given number of subplots.")
            
        else:

            nrows,ncols,odd = get_rows_cols_for_subplot(num_subplots)
        
            fig = plt.figure()
            fig.suptitle(figure_title, fontsize=fontsize)
            
            axes_list = get_axes_object_for_subplots(nrows,ncols,odd, fig, sharey)
            
            for index in range(num_subplots):
                
                if sort:
                    order = df_weekly_trend_by_product.groupby([x_axis_col_names[index]])[y_axis_col_names[index]]\
                                                                            .mean().sort_values(ascending=False).index
                    sns.barplot(x = x_axis_col_names[index], 
                                y = y_axis_col_names[index], 
                                hue = hue_col_names[index], 
                                data = data, 
                                order=order,
                                ax = axes_list[index])
                else:
                    sns.barplot(x = x_axis_col_names[index], 
                                y = y_axis_col_names[index], 
                                hue = hue_col_names[index], 
                                data = data,
                                ax = axes_list[index])

            plt.subplots_adjust(left=0.125,
                                bottom=0.1, 
                                right=0.9, 
                                top=0.9, 
                                wspace=0.5, 
                                hspace=0.35)
            
            if save_path:
                plt.savefig( f"{save_path}/"+ save_file, dpi=300, bbox_inches = "tight")
                
            plt.show()
    except Exception as error:
        raise Exception('Caught this error: ' + repr(error))

def plot_line_graph(y:pd.core.frame.DataFrame,
                       x_label:str = 'Revenue',
                       y_label:str = 'Week Number',
                       trend_label:str = 'Weekly',
                       title:str = 'Title of the graph',
                       save_file:str='trend.png',
                       fig_dim_x:int=8,
                       fig_dim_y:int=4,
                       annnotate_values:bool=True,
                       save_path:str = None)->None:  
    """
    This function plots the data of given data frame to see the trend.
    
    Args:
        y:pd.core.frame.DataFrame -> expects a dataframe of one column ideally.
        x_label:str               -> Label of x axis (i.e. hour/month/week number)
        y_label:str               -> Label of y axis (i.e. revenue/sales )
        trend_label:str           -> i.e. weekly, monthly ...
        title:str                 -> Title of the graph
        save_file:str             -> 
        fig_dim_x:int        
        fig_dim_y:int
        annnotate_values:bool
        save_path:str
    """
    try:

        fig, ax = plt.subplots(figsize=(fig_dim_x, fig_dim_y))
        ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
        ax.plot(y, marker='.', linestyle='-', linewidth=0.5, label=trend_label)
        ax.set_ylabel(x_label)
        ax.set_xlabel(y_label)
        ax.set_title(title)
        ax.legend()

        if annnotate_values:
            count = 0
            for i,j in zip(y.index.values,y.values):
                if count%4==0:
                    ax.annotate(str(j),xy=(i+0.05,j), fontsize=5)
                count+=1
        
        if save_path:
            plt.savefig( f"{save_path}/"+ save_file, dpi=300, bbox_inches = "tight")

    except Exception as error:
        raise Exception('Caught this error: ' + repr(error))

def add_value_labels(ax, spacing=5)->None:
    """Add labels to the end of each bar in a bar chart.

    Arguments:
        ax:matplotlib.axes.Axes   -> The matplotlib object containing the axes
                                     of the plot to annotate.
        spacing:int               -> The distance between the labels and the bars.
    """
    try:
        # For each bar: Place a label
        for rect in ax.patches:

            y_value = rect.get_height()
            x_value = rect.get_x() + rect.get_width() / 2

            space = spacing
            # Vertical alignment for positive values
            va = 'bottom'

            # If value of bar is negative: Place label below bar
            if y_value < 0:
                # Invert space to place label below
                space *= -1
                va = 'top'

            label = "{:.1f}".format(y_value)
            ax.annotate(
                label,                      
                (x_value, y_value),         
                xytext=(0, space),          
                textcoords="offset points", 
                ha='center',                
                va=va,                      
                fontsize=5
                )                    

    except Exception as error:
        raise Exception('Caught this error: ' + repr(error))

def plot_bargraph(df:pd.core.frame.DataFrame,
                  x_axis_column:str='product',
                  y_axis_column:str='avg_order_rev',
                  hue_column_name:str = None,
                  x_label_name:str= 'Product',
                  y_label_name:str='Average Revenue per order',
                  title:str='Tirle',
                  save_file:str='barplot.png',
                  conf_interval:bool=False,
                  color_dict:dict = None,
                  save_path:str = None)->None:
    """
    This function plots the bargraph of the given two columns of the dataframe.
    
    Args:
        df:pd.core.frame.DataFrame
        x_axis_column:str               -> Dataframe Column name to put on x-axis
        y_axis_column:str               -> Dataframe Column name to put on y-axis
        hue_column_name:str             -> Dataframe Column name to put on hue
        x_label_name:str
        y_label_name:str
        title:str
        save_file:str
        color_dict:dict
        save_path:str
    """

    try:    
        order = df.groupby([x_axis_column])[y_axis_column].mean().sort_values(ascending=False).index
        ax = None
        
        if conf_interval:
            ax = sns.barplot(x = x_axis_column, y = y_axis_column, hue=hue_column_name, data=df, order=order, palette = color_dict)
        else:
            ax = sns.barplot(x = x_axis_column, y = y_axis_column, hue=hue_column_name, data=df, order=order, ci=None, palette = color_dict)

        ax.set(xlabel=x_label_name, ylabel=y_label_name)
        ax.set_title(title)

        # #plot bar values
        add_value_labels(ax)

        if save_path:
            plt.savefig( f"{save_path}/"+ save_file, dpi=300, bbox_inches = "tight")

    except Exception as error:
        raise Exception('Caught this error: ' + repr(error))

def plot_highlighted_sphagetti_graph(df,
                                     unique_index_name:str='index',
                                     highlight_column:str='D',
                                     highlight_line_color:str='orange',
                                     line_color:str = 'grey',
                                     y_label:str='num_orders',
                                     x_label:str='Week Number',
                                     title:str = "Evolution of vs other",
                                     save_file:str='highlighted_sphagetti.png',
                                     figsize_dpi:int=96,
                                     save_path:str = None)->None:  
    """
    This function plots sphagetti graph and highlights a particular line plot
    given data frame and associated parameters.
    
    Args:
        df:pd.core.frame.DataFrame
        unique_index_name:str
        highlight_column:str     -> Column name to highlight
        highlight_line_color:str
        line_color:str
        unique_index_name:list   -> index column name of the dataframe
        y_label:str     
        x_label:str     
        title:str       
    
    Returns: 
        Updated dataframe-> consists of grouped columns and calculated result as a new column.
    
    """  

    try:
        plt.style.use('seaborn-darkgrid')

        # set figure size
        plt.figure(figsize=(480/figsize_dpi, 480/figsize_dpi), dpi=figsize_dpi)

        # plot multiple lines
        for column in df.drop(unique_index_name, axis=1):
            plt.plot(df[unique_index_name], df[column], marker='', color= line_color, linewidth=1, alpha=0.4)


        plt.plot(df[unique_index_name], df[highlight_column], marker='', color=highlight_line_color, linewidth=4, alpha=0.7)

        # Change x axis limit
        plt.xlim(df[unique_index_name].iloc[0]-1,df[unique_index_name].iloc[-1]+1)

        # Annotate the plot: hardcoded the text x-axis~26.2
        num=0
        for i in df.values[df.shape[0]-1][1:]:
            num+=1
            name=list(df)[num]
            if name != highlight_column:
                plt.text(26.2, i, name, horizontalalignment='left', size='small', color=line_color)

        # And add a special annotation for the group we are interested in
        plt.text(26.2, df[highlight_column].tail(1), '{}'.format(highlight_column), horizontalalignment='left', size='small', color='orange')

        plt.title(title,\
                  loc='center', 
                  fontsize= 10, 
                  fontweight=0)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        
        if save_path:
            plt.savefig( f"{save_path}/"+ save_file, dpi=300, bbox_inches = "tight")
            
        # Show the graph
        plt.show()

    except Exception as error:
        raise Exception('Caught this error: ' + repr(error))