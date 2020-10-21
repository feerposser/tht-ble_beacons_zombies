import time

from beacontools import BeaconScanner, EddystoneFilter, \
    EddystoneUIDFrame, EddystoneTLMFrame, EddystoneURLFrame


def read_callback(bt_addr, rssi, packet, additional_info):
    print(packet, ":", rssi)
    print(bt_addr)
    print(additional_info)
    print("-"*100)
    time.sleep(10)


def read_ble():
    scanner = BeaconScanner(
        read_callback,
        device_filter=EddystoneFilter(namespace="edd1ebeac04e5defa017"),
        packet_filter=[EddystoneUIDFrame,
                       EddystoneTLMFrame,
                       EddystoneURLFrame])
    scanner.start()
    time.sleep(5)
    scanner.stop()


read_ble()
