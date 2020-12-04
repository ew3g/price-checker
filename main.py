#from scraper import Scraper
from configProperties import ConfigProperties
from drive import Drive
import sys

configProperties = ConfigProperties()
#scraper = Scraper()

DRIVE_FOLDER_ID = configProperties.get_config_value('DRIVE_FOLDER_ID')
folder = None
if not DRIVE_FOLDER_ID:
    drive = Drive()
    folder = drive.create_folder('price_checker')
    #.create_google_spreadsheet('price_checker')
    DRIVE_FOLDER_ID = folder["id"]
    #print(folder)
    if DRIVE_FOLDER_ID:
        configProperties.save_config_value('DRIVE_FOLDER_ID', DRIVE_FOLDER_ID)
    else:
        sys.exit()



#scraper.get_product_details("https://www.amazon.com.br/GALAX-GeForce-1-Click-192-Bit-26NRL7HPX7OC/dp/B07NF7KB62/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=rtx+2060&qid=1606765964&sr=8-1");