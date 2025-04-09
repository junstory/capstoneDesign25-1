import bluetooth

target_name = "Jun"
target_address = None

nearby_devices = bluetooth.discover_devices()
print("found %d devices" % len(nearby_devices))
print("found device info")
for i in range(len(nearby_devices)):
    print(bluetooth.lookup_name(nearby_devices[i]), nearby_devices[i])
print("found device info end")
for bdaddr in nearby_devices:
    if target_name == bluetooth.lookup_name( bdaddr ):
        target_address = bdaddr
        break

if target_address is not None:
    print ("found target bluetooth device with address ", target_address)
else:
    print ("could not find target bluetooth device nearby")