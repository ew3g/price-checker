#from scraper import Scraper
from configProperties import ConfigProperties
from drive import Drive
import sys

configProperties = ConfigProperties()
#scraper = Scraper()

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


for p in configProperties.get_products():
    drive = Drive()
    #print(dir(drive.open_google_spreadsheet(p.spreadsheet_id).sheet1))
    worksheet = drive.open_google_spreadsheet(p.spreadsheet_id).sheet1
    print(drive.next_available_row2(worksheet))
    #print(dir(worksheet))
    #print(worksheet.range('A1:A5'))
    if not p.spreadsheet_id:
        drive = Drive()
        spreadsheet = drive.create_google_spreadsheet(p.name, DRIVE_FOLDER_ID)
        
        if spreadsheet:
            configProperties.save_value(p.name, 'spreadsheet.id', spreadsheet.id)
            print(dir(spreadsheet))
#scraper.get_product_details("https://www.amazon.com.br/GALAX-GeForce-1-Click-192-Bit-26NRL7HPX7OC/dp/B07NF7KB62/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=rtx+2060&qid=1606765964&sr=8-1");