""" Provides an SMBus class for use on micropython """

import gc

try:
    from machine import I2C
    gc.collect()
except ImportError:
    raise ImportError("Can't find the micropython machine.I2C class: "
                      "perhaps you don't need this adapter?")


class SMBus():

    def __init__(self, i2c):
        """Provides an 'SMBus' module which supports some of the py-smbus i2c methods, as well as being a subclass of machine.I2C.

        Hopefully this will allow you to run code that was targeted at
        py-smbus unmodified on micropython.

	    Use it like you would the machine.I2C class:

            from SMBus import SMBus

            bus = SMBus(1, pins=('G15','G10'), baudrate=100000)
            bus.read_byte_data(addr, register)
            ... etc

        Args:
            i2c (machine.I2C): I2C Channel.
	"""

        self._i2c = i2c

    def read_byte_data(self, addr, register):
        """ Read a single byte from register of device at addr
            Returns a single byte """
        return self._i2c.readfrom_mem(addr, register, 1)[0]

    def read_i2c_block_data(self, addr, register, length):
        """ Read a block of length from register of device at addr
            Returns a bytes object filled with whatever was read """
        return self._i2c.readfrom_mem(addr, register, length)

    def write_byte_data(self, addr, register, data):
        """ Write a single byte from buffer `data` to register of device at addr
            Returns None """
        # writeto_mem() expects something it can treat as a buffer
        data = bytearray(data)
        return self._i2c.writeto_mem(addr, register, data)

    def write_i2c_block_data(self, addr, register, data):
        """ Write multiple bytes of data to register of device at addr
            Returns None """
        # writeto_mem() expects something it can treat as a buffer
        data = bytearray(data)
        return self._i2c.writeto_mem(addr, register, data)

    # The follwing haven't been implemented, but could be.
    def read_byte(self, *args, **kwargs):
        """ Not yet implemented """
        raise RuntimeError("Not yet implemented")

    def write_byte(self, *args, **kwargs):
        """ Not yet implemented """
        raise RuntimeError("Not yet implemented")

    def read_word_data(self, *args, **kwargs):
        """ Not yet implemented """
        raise RuntimeError("Not yet implemented")

    def write_word_data(self, *args, **kwargs):
        """ Not yet implemented """
        raise RuntimeError("Not yet implemented")
        