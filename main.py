import time
from RFT_UART import *

PORT = "/dev/tty.usbserial-DB00G423"

if __name__ == "__main__":
    rft = RFTseries(PORT)
    rft.sendCommand(COMMAND_STOP_FT_DATA_OUTPUT)
    time.sleep(0.1)
    rft.ser.flush()
    rft.sendCommand(COMMNAD_READ_MODEL_NAME)
    time.sleep(0.1)
    print(responseReadModelName(rft.getResponse(ID_READ_MODEL_NAME)))
    rft.sendCommand(COMMAND_READ_SERIAL_NUMBER)
    time.sleep(0.1)
    print(responseReadSerialNUmber(rft.getResponse(ID_READ_SERIAL_NUMBER)))
    rft.sendCommand(COMMAND_READ_BAUDRATE)
    time.sleep(0.1)
    print(responseReadBaudrate(rft.getResponse(ID_READ_BAUDRATE)))
    rft.sendCommand(COMMAND_START_FT_DATA_OUTPUT)
    time.sleep(0.1)
    ok = False
    while not ok:
        rft.softTare()
        # print(responseReadFTData(rft.getResponse(ID_START_FT_DATA_OUTPUT)))
        print(rft.getTareFT())
        time.sleep(1/100)
        rft.ser.flush()
        check = input("is ok? [y/n]")
        if check == 'y' or check == 'Y' or check =='':
            ok = True
    while True:
        # print(responseReadFTData(rft.getResponse(ID_START_FT_DATA_OUTPUT)))
        print(f"{rft.getTareFT()[0]:>9.4f}, {rft.getTareFT()[1]:>9.4f}, {rft.getTareFT()[2]:>9.4f}, {rft.getTareFT()[3]:>9.4f}, {rft.getTareFT()[4]:>9.4f}, {rft.getTareFT()[5]:>9.4f}")
        time.sleep(1/50)
        rft.ser.flush()
    rft.sendCommand(COMMAND_STOP_FT_DATA_OUTPUT)
