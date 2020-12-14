# Price-Checker

[Read in English](link)
Price-Checker é um script em Python que varre sites e produtos pré-configurados e grava o valor em planilhas google no drive do usuário parametrizado

## Instalação
Utilize o package manager [pip](https://pip.pypa.io/en/stable/) para instalar todas as libs necessárias e depois execute:
```bash
pip install -r requirements.txt
```

Edite o arquivo config/configs.ini e crie uma nova configuração para cada produto que quiser monitorar no seguinte exemplo:

```
[NOME_PRODUTO/PRODUCT_NAME]
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

Tenha uma conta no [Google Cloud Console](https://console.cloud.google.com)

Crie um projeto para o price-checker no Google Cloud Console

Crie credenciais de conta de serviço para o projeto, instruções neste [link](https://cloud.google.com/iam/docs/creating-managing-service-account-keys)

Salve o json(gerado como abaixo) no arquivo config/keys/pck.json
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
## Uso

```bash
python main.py
```

Após executar o script, acessar [Compartilhados Comigo](https://drive.google.com/drive/shared-with-me) no Google Drive. As planilhas com os dados coletados estarão dentro da pasta price-checker.

## Contribuição
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Licença
[GNU GENERAL PUBLIC LICENSE](https://www.gnu.org/)

## Agradecimentos
Código fonte para :thanking: [Google Drive Integration on Python Gist](https://gist.github.com/miohtama/f988a5a83a301dd27469). Créditos para [miohtama](https://gist.github.com/miohtama).