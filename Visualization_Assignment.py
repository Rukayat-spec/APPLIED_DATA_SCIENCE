# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 17:35:24 2023

@author: ibrah

"""

# Import-libraries
import pandas as pd

import matplotlib.pyplot as plt


# Load fuel_exports data into Pandas DataFrame
def load_export_data(countries):

    """The function loads export data which is a % of merchandise
    exports from the World Bank Dataset

    Keyword Argument:
    countries (list): List of country names considered for the study.

    Returns:
    A dataframe containing fuel exports data for 6 countries
    from 2012 to 2021.

    """

    # Load the dataset into a Pandas DataFrame
    data_f = pd.read_csv('FUEL_EXPORT_DATA.csv', skiprows=3, index_col=1)

    # Filter the world dataframe by the list of world's top fuel export countries
    new_df = data_f[(data_f['Country Name'].isin(countries))]

    # Filter with list of years for the study
    years = [str(year) for year in range(2012, 2022)]

    # generate a new data Frame
    new_df = new_df[['Country Name'] + years]

    return new_df


#selecting the countries
countries = ['Saudi Arabia', 'United Kingdom', 'Russian Federation', 'Nigeria', 'Angola', 'Qatar']

print(load_export_data(countries))

#passing returned dataframe into a new variable export_df
export_df = load_export_data(countries)



#Visualisation 1

def lineplot_export(countries):

    """The function creates a graph in the form of a line chart that shows the
    fuel export data of six different countries over the years 2012 to 2021

    Keyword Argument:
    countries (list): List of countries for the study.

    Return:
    The line plot showing fuel exports for the countries vs years

    """

    # Transposing plot_df, so that the years can be the index of the dataframe
    plot_data = export_df.set_index('Country Name').T

    # Loop over the countries and plot each one separately
    for country in plot_data:
        plot_data[country]
        plt.plot(plot_data.index.astype(int), plot_data[country], label= country)

    # Add title, legend, and labels to plot
    #plt.title('FUEL EXPORTS (% MERCHANDISE EXPORTS) FROM 2012 to 2021', fontsize = 9)
    plt.legend(loc=3)
    plt.xlabel('Year')
    plt.ylabel('Fuel Exports')

    # Save the plot
    plt.savefig('Lineplot.png')

    # Show the plot
    plt.show()



#Visualisation 2

# Generating data for Pie chart
export_2012 = export_df.iloc[:,[0,1]]
print(export_2012)

export_2021 = export_df.iloc[:,[0,10]]
print(export_2021)

def pie_chart(export_2012, export_2021):

    """ The function generates a pie chart that presents the % of each
    country's fuel exports in relation to the total fuel exports.

    Keyword Argument:export_2012:A data frame comprising the names of countries and their
    respective fuel export quantities for the year 2021.
    export_2021: A data frame comprising the names of countries and their
    respective fuel export quantities for the year 2021.

    Return:A pie chart of fuel exports distribution for 2012 and 2021.

    """

    plt.figure(figsize=[15,15])

    #creating a subplot that shows fuel export for 2012 and 2021
    plt.subplot(2, 2, 1).set_title('FUEL_EXPORTS 2012', color='r')
    plt.pie(export_2012['2012'], labels=export_2012['Country Name'], autopct= '%1.1f%%')

    plt.subplot(2, 2, 2).set_title('FUEL EXPORTS 2022', color='r')
    plt.pie(export_2021['2021'], labels=export_2021['Country Name'], autopct= '%1.1f%%')

    #Save the plot
    plt.savefig('Pie_chart.png')

    #Show the plot
    plt.show()


#Visualisation 3

def bar_chart(angola_data):

    """ The function generates a bar chart that represents fuel exports OF Angola
    data over the period between 2012 and 2021.

    Keyword Argument:angola_data:a dataframe showing Angola's exports from 2012 to 2021

    Return: A bar chart showing Angola's fuel exports from 2012 to 2022.

    """

    plt.figure(figsize=[12,8])
    plt.bar(angola_data.index, angola_data.values, color='g')

    plt.xlabel('Year')
    plt.ylabel('Fuel Exports')
    plt.title('ANGOLA FUEL EXPORTS FROM 2012-2021')

    #Save the plot
    plt.savefig('bar_chart.png')

    #Show the plot
    return plt.show()

angola_data = export_df.iloc[0,1:]
print(angola_data)

print(lineplot_export(countries))
print(pie_chart(export_2012, export_2021))
print(bar_chart(angola_data))













