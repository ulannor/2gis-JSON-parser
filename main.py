import parser_functions as pf
import pandas as pd

filename: str = 'нотариальные услуги'

filepath = f'.\\datasource\\{filename}.csv'

dctlist = pf.json_processer(filepath)

df = pd.DataFrame(dctlist)

df.to_csv(f'.\\output\\{filename}.csv', index=False)

