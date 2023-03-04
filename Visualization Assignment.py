# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 17:35:24 2023

@author: ibrah

"""

# Import-libraries
import matplotlib.pyplot as plt

import pandas as pd


# Load fuel_exports data into Pandas DataFrame
def load_export_data(countries):

    """The function loads export data which is a proportion of merchandise
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

    """ This function generates a line plot illustrating the fuel exports
    of six countries from 2012 to 2021.

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
export_2021 = export_df.iloc[:,[0,10]]

def pie_chart(export_2012, export_2021):

    """ function creates a pie chart that displays the percentage of each
    country's fuel exports in relation to the world's total fuel exports.

    keyword Argument:export_2012:A data frame comprising the names of countries and their
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
















