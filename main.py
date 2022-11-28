import parser_functions as pf
import pandas as pd


'''Enter the name of the file with JSON data'''

filename: str = 'нотариальные услуги'

filepath = f'.\\datasource\\{filename}.csv'

dctlist = pf.json_processer(filepath)

df = pd.DataFrame(dctlist)

df.to_csv(f'.\\output\\{filename}.csv', index=False)

