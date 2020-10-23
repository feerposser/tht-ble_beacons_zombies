from statistics import median
import time

from beacontools import BeaconScanner, \
    EddystoneFilter, EddystoneUIDFrame

rssi_data = []

rssi_readed = []


def read_callback(bt_addr, rssi, packet, additional_info):
    print(rssi)
    rssi_readed.append(rssi)


def read_ble(sleep_time=1, loops=2):
    for loop in range(0, loops):
        scanner = BeaconScanner(
            read_callback,
            device_filter=EddystoneFilter(namespace="edd1ebeac04e5defa017"),
            packet_filter=[EddystoneUIDFrame]
        )

        scanner.start()
        time.sleep(sleep_time)
        scanner.stop()


def create_rssi_median():
    if len(rssi_readed) > 0:
        return median(rssi_readed)
    return None


def is_running():
    try:
        print("está correndo?")
        if (rssi_data[-2]+rssi_data[-3]) / 2 > rssi_data[-1]:
            print("sim")
            return True
        print("não")
        return False
    except Exception as e:
        print(e)


def run():
    while True:
        rssi_readed.clear()
        read_ble()
        median = create_rssi_median()

        if median:
            rssi_data.append(median)

        if len(rssi_data) > 3:
            is_running()


if __name__ == "__main__":
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(l[-5:-1])
    # run()
