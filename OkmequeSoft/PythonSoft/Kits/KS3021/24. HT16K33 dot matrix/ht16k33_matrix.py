import machine
showbytes = 0
class ht16k33_matrix:

    _HT16K33_BLINK_CMD = const(0x80)
    _HT16K33_BLINK_DISPLAYON = const(0x01)
    _HT16K33_CMD_BRIGHTNESS = const(0xE0)
    _HT16K33_OSCILATOR_ON = const(0x21)
    
    def __init__(self,dt,clk,bus,addr):
        self.addr = addr
        self.i2c = machine.I2C(bus,sda=machine.Pin(dt),scl=machine.Pin(clk))
        self.setup()
        
    def setup(self):
        self.reg_write(_HT16K33_OSCILATOR_ON,0x00) # 00100001 turn on multiplexing
        self.reg_write(_HT16K33_BLINK_CMD | _HT16K33_BLINK_DISPLAYON,0x00)
        self.set_brightness(15)
       
    def show_char(self, c):
        bytes = bytearray()  # 是可变的二进制数据(byte)
        global showbytes
        for item in c:
            temp = item
            for i in range(8):
                if temp & 0x01:
                    showbytes |= 0x01
                showbytes <<= 1
                temp >>= 1
            bytes.append( ((showbytes & 0xFE)<<0)|((showbytes & 0x01)>>7) )  # 往右移的位数，再判断01
            #bytes.append((item & 0x01)<<7)
            bytes.append(0x00)
        self.i2c.writeto_mem(self.addr, 0x00, bytes)       
    
    def set_brightness(self,brightness):
        self.reg_write(_HT16K33_CMD_BRIGHTNESS | brightness,0x00)

    def reg_write(self, reg, data):
        msg = bytearray()
        msg.append(data)
        self.i2c.writeto_mem(self.addr, reg, msg)
