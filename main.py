import parser_functions as pf
import output_functions as of


filename: str = 'нотариальные услуги'           # name of source data file

filepath = f'.\\datasource\\{filename}.csv'     # filepath is created

dctlist = pf.json_processer(filepath)           # list of dictionaries retrieved from original JSON

of.convert_to_csv(dctlist, filename)            # creates Excel and CSV with the dataframe from the list

of.log_appender(dctlist)                        # optional: updates the log.json with the list and deduplicates itself based on 2GIS URL
                                                # and creates Excel and CSV from it in the 'merged' directory