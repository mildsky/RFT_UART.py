from ctypes import c_short
def responseReadModelName(response):
    # 1~15: model name in ASCII code
    return response[1:].decode('utf-8')
def responseReadSerialNUmber(response):
    # 1~15: serial number in ASCII code
    return response[1:].decode('utf-8')
def responseReadFirmwareVersion(response):
    # 1~15: firmware version in ASCII code
    return response[1:].decode('utf-8')
def responseSetBaudrate(response):
    # 1: result of command processing [1: success, 0: fail]
    # 2: error code [1: unsupported command, 2: out of range, 3: failed to set parameter]
    return response[1], response[2]
def responseReadBaudrate(response):
    # 1: current buadrate
    # 2: buadrate to set at next boot of sensor
    return response[1], response[2]
def responseSetFilter(response):
    # 1: result of command processing [1: success, 0: fail]
    # 2: error code [1: unsupported command, 2: out of range, 3: failed to set parameter]
    return response[1], response[2]
def responseReadFilter(response):
    # 1: filter type
    # 2: filter parameter
    return response[1], response[2]
def responseReadFTData(response):
    # 1: Fx upper byte, 2: Fx lower byte
    # 3: Fy upper byte, 4: Fy lower byte
    # 5: Fz upper byte, 6: Fz lower byte
    # 7: Tx upper byte, 8: Tx lower byte
    # 9: Ty upper byte, 10: Ty lower byte
    # 11: Tz upper byte, 12: Tz lower byte
    # 13: state of overload
    Fx = c_short(response[1]*256 + response[2]).value/50
    Fy = c_short(response[3]*256 + response[4]).value/50
    Fz = c_short(response[5]*256 + response[6]).value/50
    Tx = c_short(response[7]*256 + response[8]).value/1000
    Ty = c_short(response[9]*256 + response[10]).value/1000
    Tz = c_short(response[11]*256 + response[12]).value/1000
    return Fx, Fy, Fz, Tx, Ty, Tz, response[13]
def responseStartFTDataOutput(response):
    # 1: Fx upper byte, 2: Fx lower byte
    # 3: Fy upper byte, 4: Fy lower byte
    # 5: Fz upper byte, 6: Fz lower byte
    # 7: Tx upper byte, 8: Tx lower byte
    # 9: Ty upper byte, 10: Ty lower byte
    # 11: Tz upper byte, 12: Tz lower byte
    # 13: state of overload
    Fx = c_short(response[1]*256 + response[2]).value/50
    Fy = c_short(response[3]*256 + response[4]).value/50
    Fz = c_short(response[5]*256 + response[6]).value/50
    Tx = c_short(response[7]*256 + response[8]).value/1000
    Ty = c_short(response[9]*256 + response[10]).value/1000
    Tz = c_short(response[11]*256 + response[12]).value/1000
    return Fx, Fy, Fz, Tx, Ty, Tz, response[13]
def responseSetDataOutputRate(response):
    # 1: result of command processing [1: success, 0: fail]
    # 2: error code [1: unsupported command, 2: out of range, 3: failed to set parameter]
    return response[1], response[2]
def responseReadDataOutputRate(response):
    # 1: data output rate
    return response[1]
def responseReadCountOverloadOccurrence(response):
    # 1: # of overload occurrence of Fx
    # 2: # of overload occurrence of Fy
    # 3: # of overload occurrence of Fz
    # 4: # of overload occurrence of Tx
    # 5: # of overload occurrence of Ty
    # 6: # of overload occurrence of Tz
    # 7: Maximum # of overload occurrence: 255
    return response[1], response[2], response[3], response[4], response[5], response[6], response[7]