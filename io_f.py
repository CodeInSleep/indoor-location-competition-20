from dataclasses import dataclass

import re
import pandas as pd
import numpy as np
import pdb

from constants import *
from utils import flatten_dict

class UnknownSensorException(Exception):
    pass

@dataclass
class ReadData:
    acce: np.ndarray
    acce_uncali: np.ndarray
    gyro: np.ndarray
    gyro_uncali: np.ndarray
    magn: np.ndarray
    magn_uncali: np.ndarray
    ahrs: np.ndarray
    wifi: np.ndarray
    ibeacon: np.ndarray
    waypoint: np.ndarray


def read_data_file(data_filename):
    acce = []
    acce_uncali = []
    gyro = []
    gyro_uncali = []
    magn = []
    magn_uncali = []
    ahrs = []
    wifi = []
    ibeacon = []
    waypoint = []

    with open(data_filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line_data in lines:
        line_data = line_data.strip()
        if not line_data or line_data[0] == '#':
            continue

        line_data = line_data.split('\t')

        if line_data[1] == 'TYPE_ACCELEROMETER':
            acce.append([int(line_data[0]), float(line_data[2]), float(line_data[3]), float(line_data[4])])
            continue

        if line_data[1] == 'TYPE_ACCELEROMETER_UNCALIBRATED':
            acce_uncali.append([int(line_data[0]), float(line_data[2]), float(line_data[3]), float(line_data[4])])
            continue

        if line_data[1] == 'TYPE_GYROSCOPE':
            gyro.append([int(line_data[0]), float(line_data[2]), float(line_data[3]), float(line_data[4])])
            continue

        if line_data[1] == 'TYPE_GYROSCOPE_UNCALIBRATED':
            gyro_uncali.append([int(line_data[0]), float(line_data[2]), float(line_data[3]), float(line_data[4])])
            continue

        if line_data[1] == 'TYPE_MAGNETIC_FIELD':
            magn.append([int(line_data[0]), float(line_data[2]), float(line_data[3]), float(line_data[4])])
            continue

        if line_data[1] == 'TYPE_MAGNETIC_FIELD_UNCALIBRATED':
            magn_uncali.append([int(line_data[0]), float(line_data[2]), float(line_data[3]), float(line_data[4])])
            continue

        if line_data[1] == 'TYPE_ROTATION_VECTOR':
            ahrs.append([int(line_data[0]), float(line_data[2]), float(line_data[3]), float(line_data[4])])
            continue

        if line_data[1] == 'TYPE_WIFI':
            sys_ts = line_data[0]
            ssid = line_data[2]
            bssid = line_data[3]
            rssi = line_data[4]
            lastseen_ts = line_data[6]
            wifi_data = [sys_ts, ssid, bssid, rssi, lastseen_ts]
            wifi.append(wifi_data)
            continue

        if line_data[1] == 'TYPE_BEACON':
            ts = line_data[0]
            uuid = line_data[2]
            major = line_data[3]
            minor = line_data[4]
            rssi = line_data[6]
            ibeacon_data = [ts, '_'.join([uuid, major, minor]), rssi]
            ibeacon.append(ibeacon_data)
            continue

        if line_data[1] == 'TYPE_WAYPOINT':
            waypoint.append([int(line_data[0]), float(line_data[2]), float(line_data[3])])

    acce = np.array(acce)
    acce_uncali = np.array(acce_uncali)
    gyro = np.array(gyro)
    gyro_uncali = np.array(gyro_uncali)
    magn = np.array(magn)
    magn_uncali = np.array(magn_uncali)
    ahrs = np.array(ahrs)
    wifi = np.array(wifi)
    ibeacon = np.array(ibeacon)
    waypoint = np.array(waypoint)

    return ReadData(acce, acce_uncali, gyro, gyro_uncali, magn, magn_uncali, ahrs, wifi, ibeacon, waypoint)



def get_sensor_fields(sensor_type):
    return SENSOR_FIELDS[sensor_type]

# def read_path_data(fpath, prefix=None):
#     if prefix:
#         fpath = os.path.join(prefix, fpath)
        
#     with open(fpath) as pathfile:
#         pathdata = pathfile.readlines()
        
#     # parse path data here
#     return pathdata

def parse_line(l):
    data_type = METADATA

    timestamp = None
    payload = {} 
    if l.startswith("#"):
        matches = re.findall(r"((\w+):(\w+))+", l, re.MULTILINE | re.UNICODE)
        for m in matches:
            payload[m[1]] = m[2]
    else:
        sensor_data = l.split("\t")
        
        sensor_type = sensor_data[1]
        if sensor_type not in SENSOR_FIELDS:
            raise UnknownSensorException(f"unknown sensor type: {sensor_type}")
            
        sensor_fields = get_sensor_fields(sensor_type)
        sensor_values = sensor_data[2:]
        if len(sensor_fields) != len(sensor_values):
            assert f"sensor fields and values must be same length for {sensor_type}"
        
        timestamp = sensor_data[0]
        for (k, v) in zip(sensor_fields, sensor_values):
            try:
                v = float(v.rstrip())
            except:
                pass
            payload[k] = v
    
        data_type = SENSORDATA
    
    return timestamp, payload, data_type

def read_path_data(path_file):
    metadata = {}
    sensor_data = {}

    with open(path_file, 'r', encoding='utf-8') as f:
        for line_no, line in enumerate(f.readlines()):
            try:
                ts, payload, dtype = parse_line(line)
                if ts is not None:
                    ts = int(ts)
            except UnknownSensorException:
                continue
            
            payload["TIMESTAMP"] = ts
            
            if dtype == METADATA:
                metadata.update(payload)
            elif dtype == SENSORDATA:
                sensor_data[line_no] = payload
            else:
                assert False
    return metadata, pd.DataFrame(sensor_data).T

def get_gt_path(df):
    return df.loc[df.loc[:, "X"].notnull(), ["X", "Y"]].reset_index().values

def get_sensor_values(df, sensor_names, with_ts=False, reset_index=False, to_val=False, dropna=True):
    sensor_fields = ["TIMESTAMP"] if with_ts else []
    for sensor in sensor_names:
        sensor_fields.extend(SENSOR_FIELDS[sensor])
    
    sensor_values = df.loc[:, sensor_fields]
    if reset_index:
        sensor_values = sensor_values.reset_index()

    if dropna:
        sensor_values = sensor_values.dropna()
    
    if to_val:
        sensor_values = sensor_values.values
    return sensor_values
