#from scraper import Scraper
from configProperties import ConfigProperties
from drive import Drive
import sys

configProperties = ConfigProperties()
configProperties.get_products()
#scraper = Scraper()
'''
DRIVE_FOLDER_ID = configProperties.get_value('DEFAULT', 'default_drive_folder_id')

folder = None
if not DRIVE_FOLDER_ID:
    drive = Drive()
    folder = drive.create_folder('price_checker')
    DRIVE_FOLDER_ID = folder['id']

    if not DRIVE_FOLDER_ID:
        print('ERROR: was not possible to create the drive folder for price-checker')
        sys.exit()

    configProperties.save_value('DEFAULT', 'default_drive_folder_id', DRIVE_FOLDER_ID)
'''
'''

for p in configProperties.get_products():
    drive = Drive()
    #worksheet = None
    #print(drive.next_available_row2(worksheet))
    #print(dir(worksheet))
    #print(worksheet.range('A1:A5'))
    if not p.spreadsheet_id:
        drive = Drive()
        spreadsheet = drive.create_google_spreadsheet(p.name, DRIVE_FOLDER_ID)
        
        if spreadsheet:
            p.spreadsheet_id = spreadsheet.id
            configProperties.save_value(p.name, 'spreadsheet.id', spreadsheet.id)
            
    worksheet = drive.open_google_spreadsheet(p.spreadsheet_id).sheet1
    available_row = drive.next_available_row(worksheet)
    last_row = int(available_row) - 1
    last_value_cell = None
    if last_row > 0:
        last_cell = 'A' + str(last_row)
        last_value_cell = worksheet.acell(last_cell).value
        #print(last_value_cell)
    
    save = 'teste1w'

    if last_value_cell is not None:
        if last_value_cell == save:
            print('igual')
        else:
            print('diferente')
            cell_edit = 'A' + str(available_row)
            worksheet.update(cell_edit, save)
'''

#scraper.get_product_details("https://www.amazon.com.br/GALAX-GeForce-1-Click-192-Bit-26NRL7HPX7OC/dp/B07NF7KB62/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=rtx+2060&qid=1606765964&sr=8-1");