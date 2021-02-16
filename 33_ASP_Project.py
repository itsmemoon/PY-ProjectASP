import pandas as pd
import matplotlib.pyplot as plt
import unittest

def create_data():
    data = pd.DataFrame(
        {"Visitors": [0, 0, 0, 0, 0, 0, 70261,	1018843, 890727, 0, 4226203, 316647, 110959,
                1699347, 13185, 250977, 58742, 0, 32752, 205575
]},
        index=['Brunei Darussalam', 'Indonesia', 'Malaysia', 'Myanmar', 'Philippines',
                 'Thailand', 'Vietnam', 'China', 'Hong Kong SAR', 'Taiwan', 'Japan',
                 'South Korea', 'Bangladesh', 'India', 'Pakistan', 'Sri Lanka', 'Iran',
                 'Israel', 'Kuwait', 'Saudi Arabia'])

    return data

class Analysis:
    def top3(self):
        Countries = pd.read_excel('IMVA.xlsx')
        print(Countries)

        Countries = Countries.replace(['na'], 0 )
        print(Countries)

        print(Countries.columns)

        indexOne = Countries.loc[Countries.Periods == '1978 Jan', :]
        print(indexOne)
        indexTwo = Countries.loc[Countries.Periods == '1987 Dec', :]
        print(indexTwo)

        CountriesData = Countries.loc[0:119,:]

        analysisChart = create_data()

        analysisChartSorted = analysisChart.sort_values(by='Visitors', ascending=False)
        print(analysisChartSorted)

        top = analysisChartSorted.head(3)
        top.plot(kind='bar', title="Top 3 in Asia (Period:1978 - 1987)",
                      figsize=(10, 10), legend=True, fontsize=12, label="Visitors")
        print(top)

        first = analysisChartSorted.index[0]
        second = analysisChartSorted.index[1]
        third = analysisChartSorted.index[2]

        ax = analysisChartSorted.plot(kind='bar', title="Total Visitors in Asia (Period:1978 - 1987)",
                      figsize=(10, 10), legend=True, fontsize=12, label="Visitors")
        plt.show()

        return [first, second, third]

a = Analysis()
print(a.top3())

class unitTest(unittest.TestCase):

    def test_analysis_1_pass(self):
        a = Analysis()
        b = a.top3()
        self.assertFalse(['Japan'] in b, False)

    def test_analysis_2_pass(self):
        a = Analysis()
        self.assertEqual(a.top3(), ['Japan', 'India', 'China'])

   # def test_analysis_3_fail(self):
      #  a = Analysis()
      #  b = a.top3()
      #  self.assertFalse('France' in a, False)

#if __name__ == '__main__':
    #unittest.main()

