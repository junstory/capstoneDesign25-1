bd_addr = "D8:3A:DD:F2:29:20"

import asyncio
from bleak import BleakClient, BleakScanner

async  def  main ():
    devices = await BleakScanner.discover()
    for d in devices:
        print(d)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print('Done!')