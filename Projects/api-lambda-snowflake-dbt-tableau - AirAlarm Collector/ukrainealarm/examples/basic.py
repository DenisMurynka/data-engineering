import asyncio
import aiohttp
from ukrainealarm.client import Client


async def main():
    async with aiohttp.ClientSession() as session:
        client = Client(session, "API-CODE")

        # All response formats are available here: https://api.ukrainealarm.com/swagger/index.html
        #global data
        #regions = await client.get_regions()
        #return data
        #print("regions list", regions)

        # all_alerts = await client.get_alerts()
        # print("all alerts", all_alerts)

        # region_alerts = await client.get_alerts(16)
        # print("alerts of region 16", region_alerts)

        # last_alert_index = await client.get_last_alert_index()
        # print("last alert index", last_alert_index)
       
        
        regions = await client.get_history(region_id=16)
        print("last 25 alerts in region ", regions)
        

asyncio.run(main())

