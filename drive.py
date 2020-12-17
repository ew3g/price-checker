from oauth2client.service_account import ServiceAccountCredentials
from apiclient.discovery import build
import gspread
from gspread.models import Spreadsheet
import logging
from constants.constants import (ConfigConstants, DriveConstants,
                                 StringConstants)
from configProperties import ConfigProperties

logger = logging.getLogger(__name__)


class Drive:

    def get_credentials(self, scopes: list) -> ServiceAccountCredentials:
        """Read Google's JSON permission file.
        https://developers.google.com/api-client-library/python/auth/service-accounts#example
        :param scopes: List of scopes we need access to
        """
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            ConfigConstants.DRIVE_KEY_PCK_FILE_PATH, scopes)
        return credentials

    def open_google_spreadsheet(self, spreadsheet_id: str) -> Spreadsheet:
        """Open sheet using gspread.
        :param spreadsheet_id: Grab spreadsheet id from URL to open.
        Like *1jMU5gNxEymrJd-gezJFPv3dQCvjwJs7QcaB-YyN_BD4*.
        """
        credentials = self.get_credentials(
            [DriveConstants.GOOGLE_SPREADSHEETS_FEEDS_URL])
        gc = gspread.authorize(credentials)
        return gc.open_by_key(spreadsheet_id)

    def create_google_spreadsheet(self, title: str,
                                  parent_folder_ids: list = None,
                                  share_domains: list = None) -> Spreadsheet:
        """Create a new spreadsheet and open gspread object for it.
        .. note ::
            Created spreadsheet is not instantly visible in your Drive search
            and you need to access it by direct link.
        :param title: Spreadsheet title
        :param parent_folder_ids: A list of strings of parent
        folder ids (if any).
        :param share_domains: List of Google Apps domain whose members get
        full access rights to the created sheet. Very handy, otherwise the
        file is visible only to the service worker itself.
        Example:: ``["redinnovation.com"]``.
        """

        credentials = self.get_credentials(
            [DriveConstants.GOOGLE_DRIVE_AUTH_URL])

        drive_api = build(DriveConstants.DRIVE_API,
                          DriveConstants.DRIVE_API_VERSION,
                          credentials=credentials)

        google_mail_address = ConfigProperties(
                    ConfigConstants.EMAIL_CONFIG_FILE_PATH).get_value(
                        ConfigConstants.DEFAULT,
                        StringConstants.GOOGLE_MAIL)

        logger.info("Creating Sheet %s", title)
        body = {
            StringConstants.NAME: title,
            StringConstants.MIME_TYPE:
                DriveConstants.MIME_TYPE_GOOGLE_SPREADSHEET,
        }

        if parent_folder_ids:
            body[StringConstants.PARENTS] = [parent_folder_ids]

        req = drive_api.files().create(body=body)
        new_sheet = req.execute()

        # Get id of fresh sheet
        spread_id = new_sheet[StringConstants.ID]

        user_permission = {
            StringConstants.TYPE: StringConstants.USER,
            StringConstants.ROLE: StringConstants.WRITER,
            StringConstants.EMAIL_ADDRESS: google_mail_address
        }

        req2 = drive_api.permissions().create(
            fileId=spread_id,
            body=user_permission,
            fields=StringConstants.ID)
        req2.execute()

        spread = self.open_google_spreadsheet(spread_id)
        return spread

    def create_folder(self, folder_name):
        body = {
            StringConstants.TITLE: folder_name,
            StringConstants.NAME: folder_name,
            StringConstants.MIME_TYPE: DriveConstants.MIME_TYPE_GOOGLE_FOLDER
        }

        credentials = self.get_credentials(
            [DriveConstants.GOOGLE_DRIVE_FILE_AUTH_URL])
        drive_api = build(DriveConstants.DRIVE_API,
                          DriveConstants.DRIVE_API_VERSION,
                          credentials=credentials)

        google_mail_address = ConfigProperties(
                    ConfigConstants.EMAIL_CONFIG_FILE_PATH).get_value(
                        ConfigConstants.DEFAULT, StringConstants.GOOGLE_MAIL)

        created_folder_id = drive_api.files().create(body=body).execute()

        user_permission = {
            StringConstants.TYPE: StringConstants.USER,
            StringConstants.ROLE: StringConstants.WRITER,
            StringConstants.EMAIL_ADDRESS: google_mail_address
        }

        drive_api.permissions().create(
            fileId=created_folder_id.get(StringConstants.ID),
            body=user_permission,
            fields=StringConstants.ID
        ).execute()

        return created_folder_id

    def next_available_row(self, wks):
        str_list = list(filter(None, wks.col_values(1)))
        return str(len(str_list) + 1)
