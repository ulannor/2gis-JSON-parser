import parser_functions as pf
import output_functions as of

'''Enter the name of the file with JSON data'''

filename: str = 'нотариальные услуги'

filepath = f'.\\datasource\\{filename}.csv'     #Filepath is created

dctlist = pf.json_processer(filepath)           #List of dictionaries with JSON data

of.convert_to_csv(dctlist, filename)            #Creates Excel and CSV with the dataframe from the list

of.log_appender(dctlist)                        #Optional: updates the log.json with the list and deduplicates itself based on 2GIS URL
