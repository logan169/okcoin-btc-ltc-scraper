from cryptoScraper.currencyScraper import okcoin_btc_usd,okcoin_ltc_usd
from apscheduler.schedulers.blocking import BlockingScheduler
from pytz import utc
from db.sqlite_init import create_Tables

###init
create_Tables()

###main
def main(time,missTime):
    """Run tick() at the interval of every time seconds."""
    scheduler = BlockingScheduler(timezone=utc)
    #scheduler = BlockingScheduler(timezone=utc, executors = {'default': ProcessPoolExecutor(max_workers=12)})

    ###############         okcoin              ################
    scheduler.add_job(okcoin_btc_usd, 'interval', seconds=time,max_instances=3,misfire_grace_time=missTime)
    scheduler.add_job(okcoin_ltc_usd, 'interval', seconds=time,max_instances=3,misfire_grace_time=missTime)
    
    try:
        scheduler.start()

    except (KeyboardInterrupt, SystemExit):
        pass

if __name__ == '__main__':

    main(1.5,2) #EDIT input parameter 1st one is the time step you want to scrap data, the second is the time gap tolerance in case its late
