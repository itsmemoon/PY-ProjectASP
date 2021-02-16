import pandas as pd
import matplotlib.pyplot as plt
import unittest
class Country:
    def findTop3(self):
        countries = pd.read_excel('IMVA.xlsx')
        print(countries)

        country = countries['Periods'].str.split(expand = True)
        countries = countries.assign(country_year=pd.to_numeric(country[0]))
        countrylist = countries[(countries['country_year'] >= 1978) & (countries['country_year'] <= 1987)].iloc[0:119,:]
        out = countrylist.sum().sort_values(ascending=False)/1000
        print("The top 3 countriesIMVA.xlsx are %s, %s and %s." %(out.index[0], out.index[1], out.index[2]))



        ax=out.plot(kind='bar' , title = "Total Travellers from Asia in thousands (Period:1988 - 1998)", figsize=(10,10), legend=True, fontsize=12, label="Travellers")
        plt.show()
        return [out.index[0], out.index[1], out.index[2]]
g = Country()

print(g.findTop3())