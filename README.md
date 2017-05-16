# okcoin btc/ltc scraper
## Cryptocurrencies scraper

This repo contains an app design to connect through okcoin API every x times and get btc/ltc value.
It stock data in a sqlite database in db folder. You could then use any sql software to read db and export it in csv format.

Here is an example of data scrapped with this script:

##### db file	       timestamp  value   ask Vol  bids Vol
##### okcoin_btc_usd 1494954839 1646.94 50.717   86.199

### Disclaimer
This script was initially designed to run continuously on a raspberry pi (rpi). 
Beware that if you choose to do the same, this script is intensive in write/read cycles and may corrupt your rpi sdd card after a while. For this reason, I advice you to run it on an USB key connected to your rpi. 
I can't be held responsable in any case for any damages that could occur to your system or hardware while running this script.

#### Dependancies
- Python 3
- apscheduler


### Initialization

#### To launch the app (on your computer)
After installing dependancies type the following commands:

		$ cd App
		$ python3 main.py

The print comment of currencyScraper.py have been commented so you will not have any output.
You could decomment them for test purpose.

#### To launch the app (on your headless rpi)
Clone the repo on a USB key and plug it to your rpi. Connect through ssh to your rpi and install dependancies.
After installing dependancies type the following commands:

		$ cd <path to your USB key>
		$ cd okcoin_scraper/App
		$ nohup python3 main.py

You could now close the terminal and live your life while scrapping btc/ltc data.

##### Get back db from a headless rpi

To download db files, open a terminal on your computer and type the following command after filling <variable> tag:

		$ scp pi@<rpi_ip_adress>:<path_to_db_file> <location_where_you_wanna_save_it> 

An example could be :

		$ scp pi@192.168.1.141:/media/usb1/bitcoin_scrapper/okcoin_btc_usd.db .


Happy Data Scraping!!


