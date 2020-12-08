from oauth2client.service_account import ServiceAccountCredentials
from apiclient.discovery import build
import gspread
from gspread.models import Spreadsheet
import logging

#https://gist.github.com/miohtama/f988a5a83a301dd27469
#https://developers.google.com/drive/api/v3/search-files

logger = logging.getLogger(__name__)


class Drive:

    def get_credentials(self, scopes: list) -> ServiceAccountCredentials:
        """Read Google's JSON permission file.
        https://developers.google.com/api-client-library/python/auth/service-accounts#example
        :param scopes: List of scopes we need access to
        """
        credentials = ServiceAccountCredentials.from_json_keyfile_name('config/keys/pck.json', scopes)
        return credentials

    def open_google_spreadsheet(self, spreadsheet_id: str) -> Spreadsheet:
        """Open sheet using gspread.
        :param spreadsheet_id: Grab spreadsheet id from URL to open. Like *1jMU5gNxEymrJd-gezJFPv3dQCvjwJs7QcaB-YyN_BD4*.
        """
        credentials = self.get_credentials(['https://spreadsheets.google.com/feeds'])
        gc = gspread.authorize(credentials)
        return gc.open_by_key(spreadsheet_id)

    def create_google_spreadsheet(self, title: str, parent_folder_ids: list=None, share_domains: list=None) -> Spreadsheet:
        """Create a new spreadsheet and open gspread object for it.
        .. note ::
            Created spreadsheet is not instantly visible in your Drive search and you need to access it by direct link.
        :param title: Spreadsheet title
        :param parent_folder_ids: A list of strings of parent folder ids (if any).
        :param share_domains: List of Google Apps domain whose members get full access rights to the created sheet. Very handy, otherwise the file is visible only to the service worker itself. Example:: ``["redinnovation.com"]``.
        """

        credentials = self.get_credentials(['https://www.googleapis.com/auth/drive'])

        drive_api = build('drive', 'v3', credentials=credentials)

        logger.info("Creating Sheet %s", title)
        body = {
            'name': title,
            'mimeType': 'application/vnd.google-apps.spreadsheet',
        }

        if parent_folder_ids:
            body["parents"] = [parent_folder_ids]

        req = drive_api.files().create(body=body)
        new_sheet = req.execute()

        # Get id of fresh sheet
        spread_id = new_sheet["id"]


        user_permission = {
            'type': 'user',
            'role': 'writer',
            'emailAddress': 'edilson.w3g@gmail.com',
            #'allowFileDiscovery': True
        }

        req2 = drive_api.permissions().create(
            fileId=spread_id,
            body=user_permission,
            fields="id"
        )
        req2.execute()    

        spread = self.open_google_spreadsheet(spread_id)
        return spread

    def create_folder(self, folder_name):
        body = {
            'title': folder_name,
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }

        credentials = self.get_credentials(['https://www.googleapis.com/auth/drive.file'])
        drive_api = build('drive', 'v3', credentials=credentials)

        created_folder_id = drive_api.files().create(body = body).execute()

        user_permission = {
            'type': 'user',
            'role': 'writer',
            'emailAddress': 'edilson.w3g@gmail.com'
        }

        #credentials = get_credentials(['https://www.googleapis.com/auth/drive.file'])
        #drive_api = build('drive', 'v3', credentials=credentials)
        drive_api.permissions().create(
            fileId=created_folder_id.get('id'),
            body=user_permission,
            fields="id"
        ).execute()

        return created_folder_id

#    def next_available_row(self, sheet):
#        # looks for empty row based on values appearing in 1st N columns
#        cols = sheet.range(1, 1, sheet.row_count, 1)
#        return max([cell.row for cell in cols if cell.value]) + 1

    def next_available_row(self, wks):
        
        str_list = list(filter(None, wks.col_values(1)))  # fastest
        return str(len(str_list)+1)
