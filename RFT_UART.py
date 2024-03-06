import serial
import time
import threading
from RFT_UART_command import *
from RFT_UART_response import *

class RFTseries:
    __response = dict()
    def __init__(self, port, baud=115200):
        # default 115200 bps
        # 1 stop bit, No parity, No flow control, 8 data bits
        self.ser = serial.Serial(port, baud)
        self.ser.flush()
        self.__thread = threading.Thread(target=self.readResponseRunner)
        self.__thread.daemon = True
        self.__thread.start()
    ## Command Packet Structure
    # SOP : 0x55
    # Data Field  : 8 bytes
    # Checksum : 1 byte, summation of data field
    # EOP : 0xAA
    def sendCommand(self, command):
        if len(command) != 8:
            raise ValueError('Data field must be 8 bytes long')
        packet = b'\x55' + command + int.to_bytes(sum(command)) + b'\xAA'
        self.ser.write(packet)
        return packet
    ## Response Packet Structure
    # SOP : 0x55
    # Data Field  : 16 bytes
    # Checksum : 1 byte
    # EOP : 0xAA
    def readResponseRunner(self):
        while True:
            if self.ser.in_waiting:
                if self.ser.read() == b'\x55':
                    data = self.ser.read(16)
                    checksum = self.ser.read()
                    eop = self.ser.read()
                    responseID = data[0]
                    self.__response[responseID] = data
    def getResponse(self, responseID):
        return self.__response.get(responseID)

PORT = "/dev/tty.usbserial-DB00G423"

if __name__ == "__main__":
    rft = RFTseries(PORT)
    rft.sendCommand(COMMAND_STOP_FT_DATA_OUTPUT)
    time.sleep(1)
    rft.ser.flush()
    rft.sendCommand(COMMNAD_READ_MODEL_NAME)
    time.sleep(1)
    print(responseReadModelName(rft.getResponse(1)))
    rft.sendCommand(COMMAND_READ_SERIAL_NUMBER)
    time.sleep(1)
    print(responseReadSerialNUmber(rft.getResponse(2)))
    rft.sendCommand(COMMAND_READ_BAUDRATE)
    time.sleep(1)
    print(responseReadBaudrate(rft.getResponse(7)))
    rft.sendCommand(COMMAND_START_FT_DATA_OUTPUT)
    time.sleep(1)
    rft.sendCommand(commandSetBias(1))
    for i in range(5000):
        print(responseReadFTData(rft.getResponse(11)))
        time.sleep(1/200)