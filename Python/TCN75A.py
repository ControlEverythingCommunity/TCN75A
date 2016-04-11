# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# TCN75A
# This code is designed to work with the TCN75A_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Temperature?sku=TCN75A_I2CS#tabs-0-product_tabset-2

import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)

# TCN75A address, 0x48(72)
# Select configuration register, 0x01(01)
#		0x60(96)	12-bit ADC resolution
bus.write_byte_data(0x48, 0x01, 0x60)

time.sleep(0.5)

# TCN75A address, 0x48(72)
# Read data back from 0x00(00), 2 bytes
# cTemp MSB, cTemp LSB
data = bus.read_i2c_block_data(0x48, 0x00, 2)

# Convert the data to 12-bits
cTemp = ((data[0] * 256 + data[1]) / 16) * 0.0625
fTemp = (cTemp * 1.8) + 32

# Output data to screen
print "Temperature in Celsius : %.2f C" %cTemp
print "Temperature in Fahrenheit : %.2f F" %fTemp