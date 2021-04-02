# sensor constants
TYPE_ROTATION_VECTOR = "TYPE_ROTATION_VECTOR"
TYPE_ACCELEROMETER = "TYPE_ACCELEROMETER"
TYPE_ACCELEROMETER_UNCALIBRATED = "TYPE_ACCELEROMETER_UNCALIBRATED"
TYPE_GYROSCOPE = "TYPE_GYROSCOPE"
TYPE_GYROSCOPE_UNCALIBRATED = "TYPE_GYROSCOPE_UNCALIBRATED"
TYPE_MAGNETIC_FIELD = "TYPE_MAGNETIC_FIELD"
TYPE_MAGNETIC_FIELD_UNCALIBRATED = "TYPE_MAGNETIC_FIELD_UNCALIBRATED"
TYPE_WAYPOINT = "TYPE_WAYPOINT"
TYPE_WIFI = "TYPE_WIFI"
TYPE_BEACON = "TYPE_BEACON"

# ROTATION VECTOR FIELDS
AZIMUTH = "AZIMUTH"
PITCH = "PITCH"
ROLL = "ROLL"

# ACCELERATOR VECTOR FIELDS
X_ACCEL = "X_ACCEL"
Y_ACCEL = "Y_ACCEL"
Z_ACCEL = "Z_ACCEL"

# UNCALIBRATED ACCELERATOR VECTOR FIELDS
X_UNCALIB_ACCEL = "X_UNCALIB_ACCEL"
Y_UNCALIB_ACCEL = "Y_UNCALIB_ACCEL"
Z_UNCALIB_ACCEL = "Z_UNCALIB_ACCEL"
X_ACCEL_BIAS = "X_ACCEL_BIAS"
Y_ACCEL_BIAS = "Y_ACCEL_BIAS"
Z_ACCEL_BIAS = "Z_ACCEL_BIAS"

# GYROSCOPE VECTOR FIELDS
X_GYRO = "X_GYRO"
Y_GYRO = "Y_GYRO"
Z_GYRO = "Z_GYRO"

# UNCALIBRATED GYROSCOPE VECTOR FIELDS
X_UNCALIB_GYRO = "X_UNCALIB_GYRO"
Y_UNCALIB_GYRO = "Y_UNCALIB_GYRO"
Z_UNCALIB_GYRO = "Z_UNCALIB_GYRO"
X_GYRO_DRIFT = "X_GYRO_DRIFT"
Y_GYRO_DRIFT = "Y_GYRO_DRIFT"
Z_GYRO_DRIFT = "Z_GYRO_DRIFT"

# MAGNETOMETER VECTOR FIELDS
X_MAGN = "X_MAGN"
Y_MAGN = "Y_MAGN"
Z_MAGN = "Z_MAGN"

# UNCALIBRATED GYROSCOPE VECTOR FIELDS
X_UNCALIB_MAGN = "X_UNCALIB_MAGN"
Y_UNCALIB_MAGN = "Y_UNCALIB_MAGN"
Z_UNCALIB_MAGN = "Z_UNCALIB_MAGN"
X_MAGN_BIAS = "X_MAGN_BIAS"
Y_MAGN_BIAS = "Y_MAGN_BIAS"
Z_MAGN_BIAS = "Z_MAGN_BIAS"

# WAYPOINT VECTOR FIELDS
X = "X"
Y = "Y"

# WIFI VECTOR FIELDS
SSID = "SSID"
BSSID = "BSSID"
WIFI_RSSI = "WIFI_RSSI"
WIFI_FREQ = "WIFI_FREQUENCY"
LASTSEEN_TS = "LASTSEEN_TS"


# BEACON VECTOR FIELDS
UUID = "UUID"
MAJOR_ID = "MAJOR_ID"
MINOR_ID = "MINOR_ID"
BEACON_RSSI = "BEACON_RSSI"

# data_types
METADATA = 0
SENSORDATA = 1

SENSOR_FIELDS = {
    TYPE_ROTATION_VECTOR: [AZIMUTH, PITCH, ROLL],
    TYPE_ACCELEROMETER: [X_ACCEL, Y_ACCEL, Z_ACCEL],
    TYPE_ACCELEROMETER_UNCALIBRATED: [X_UNCALIB_ACCEL, Y_UNCALIB_ACCEL, Z_UNCALIB_ACCEL, X_ACCEL_BIAS, Y_ACCEL_BIAS, Z_ACCEL_BIAS],
    TYPE_GYROSCOPE: [X_GYRO, Y_GYRO, Z_GYRO],
    TYPE_GYROSCOPE_UNCALIBRATED: [X_UNCALIB_GYRO, Y_UNCALIB_GYRO, Z_UNCALIB_GYRO, X_GYRO_DRIFT, Y_GYRO_DRIFT, Z_GYRO_DRIFT],
    TYPE_MAGNETIC_FIELD_UNCALIBRATED: [X_MAGN, Y_MAGN, Z_MAGN],
    TYPE_MAGNETIC_FIELD: [X_UNCALIB_MAGN, Y_UNCALIB_MAGN, Z_UNCALIB_MAGN, X_MAGN_BIAS, Y_MAGN_BIAS, Z_MAGN_BIAS],
    TYPE_WAYPOINT: [X, Y],
    TYPE_WIFI: [SSID, BSSID, WIFI_RSSI, WIFI_FREQ, LASTSEEN_TS]    
}