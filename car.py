from pyb import Pin, Timer
inverse_left=True  #change it to True to inverse left wheel
inverse_right=True #change it to True to inverse right wheel

ain1 =  Pin('P1', Pin.OUT_PP)
bin1 =  Pin('P0', Pin.OUT_PP)
ain1.low()
bin1.low()

pwma = Pin('P7')
pwmb = Pin('P8')
tim = Timer(4, freq=1000)
ch1 = tim.channel(1, Timer.PWM, pin=pwma)
ch2 = tim.channel(2, Timer.PWM, pin=pwmb)
ch1.pulse_width_percent(0)
ch2.pulse_width_percent(0)

def run(left_speed, right_speed):
    if inverse_left==True:
        left_speed=(-left_speed)
    if inverse_right==True:
        right_speed=(-right_speed)

    if right_speed < 0:
        ain1.low()
        ch1.pulse_width_percent(int(abs(right_speed)))
    else:
        ain1.high()
        ch1.pulse_width_percent(100-int(abs(right_speed)))

    if left_speed < 0:
        bin1.low()
        ch2.pulse_width_percent(int(abs(left_speed)))
    else:
        bin1.high()
        ch2.pulse_width_percent(100-int(abs(left_speed)))
