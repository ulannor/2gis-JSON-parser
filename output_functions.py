import pandas as pd
import json

def convert_to_csv(dctlist, filename):
    df = pd.DataFrame(dctlist)
    column_order = df.columns[:8].tolist() + sorted(df.columns[8:].tolist())
    df_sorted = df[column_order]
    df_sorted.to_csv(f'.\\output\\{filename}.csv', index=False)
    df_sorted.to_excel(f'.\\output\\{filename}.xlsx', index=False)

def log_appender(dctlist)
    try:
        with open('.\\log\\log.json', 'r') as in_file:
            logdata = json.load(in_file)
    except FileNotFoundError:
        logdata = []

    logdata.extend(dctlist)

    undupl_logdata = list({dct['2GIS URL']: dct for dct in logdata}.values())

    with open('.\\log\\log.json', "w") as file:
        json.dump(undupl_logdata, file, ensure_ascii=False)