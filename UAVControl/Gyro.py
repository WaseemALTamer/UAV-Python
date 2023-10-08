from mpu6050 import mpu6050
import math
import time


sensor = mpu6050(0x68)

def calculate_euler_angles(accel_data):
    accel_x = accel_data['x']
    accel_y = accel_data['y']
    accel_z = accel_data['z']
    Angle_x = math.atan2(accel_x, math.sqrt(accel_y**2 + accel_z**2))
    Angle_z = math.atan2(-accel_y, math.sqrt(accel_x**2 + accel_z**2))
    gyro_data = sensor.get_gyro_data()
    gyro_z = gyro_data['z']
    yaw = gyro_z
    Angle_x_degrees = math.degrees(Angle_x)
    Angle_z_degrees = math.degrees(Angle_z)
    yaw_degrees = math.degrees(yaw)
    return Angle_x_degrees, Angle_z_degrees, yaw_degrees

def main():
    accel_data = sensor.get_accel_data()
    Angle_x_degrees, Angle_z_degrees, yaw = calculate_euler_angles(accel_data)
    return [int(Angle_x_degrees),int(Angle_z_degrees),int(yaw)]