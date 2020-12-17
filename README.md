# Price-Checker

[Read in Portuguese](https://github.com/lukeSkywallk/price-checker/blob/develop/README-pt.md)\
Price-Checker is a web crawler python script that scans products in websites and writes the prices on google spreadsheets in user's Google Drive.

## Installation
Use package manager [pip](https://pip.pypa.io/en/stable/) to install all needed libs
```bash
pip install -r requirements.txt
```

Edit the file config/configs.ini and set a new config for each product you want to monitor. E.g.

```
[PRODUCT_NAME]
spreadsheet.id=LEAVE_BLANK
kabum=PRODUCT_URL_KABUM
terabyte=PRODUCT_URL_TERABYTE
pichau=PRODUCT_URL_PICHAU
amazon=PRODUCT_URL_AMAZON

```
```
[galax_rtx_2060_6gb]
spreadsheet.id=
kabum=https://www.kabum.com.br/produto/100235/placa-de-v-deo-galax-nvidia-geforce-rtx-2060-6gb-gddr6-26nrl7hpx7oc
terabyte=https://www.terabyteshop.com.br/produto/10304/placa-de-video-galax-geforce-rtx-2060-1-click-oc-6gb-26nrl7hpx7oc-gddr6-pci-exp
pichau=https://www.pichau.com.br/hardware/placa-de-video/placa-de-video-galax-geforce-rtx-2060-6gb-gddr6-1-click-oc-192-bit-26nrl7hpx7oc
amazon=https://www.amazon.com.br/GALAX-GeForce-1-Click-192-Bit-26NRL7HPX7OC/dp/B07NF7KB62

```

The supported websites so far are: KABUM, TERABYTE, PICHAU e AMAZON.

Edit just as the example, the script will handle the other settings.

Edit the file config/email.properties and place the google mail in which the sheets with the product price data will be stored
```
[DEFAULT]
google_mail=#insira seu email google aqui / place your google mail here
```

Have a [Google Cloud Console](https://console.cloud.google.com) account

Create a project for price-checker on Google Cloud Console

Create service account credential for the projects, instructions [here](https://cloud.google.com/iam/docs/creating-managing-service-account-keys)

Save the json(generated as below) on path config/keys/pck.json
```
{
  "type": "service_account",
  "project_id": "id-project",
  "private_key_id": "id-key",
  "private_key": "-----BEGIN PRIVATE KEY-----\\n-----END PRIVATE KEY-----\n",
  "client_email": "service-account@mail",
  "client_id": "id",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "url-cert"
}
```
## Usage

```bash
python main.py
```

After running the script, go to [Shared With Me](https://drive.google.com/drive/shared-with-me) on Google Drive. The sheets with the data will be on folder price-checker

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[GNU GENERAL PUBLIC LICENSE](https://www.gnu.org/)

## Thanking
Source code for the [Google Drive Integration on Python Gist](https://gist.github.com/miohtama/f988a5a83a301dd27469). Credits to [miohtama](https://gist.github.com/miohtama).