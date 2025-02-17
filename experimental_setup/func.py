from datetime import datetime as dt
from datetime import timedelta as td
import time

import visa
import logging as l

import os


def gen_period(log, dev, source=1, period=1, period_unit="s", delay=0.15):
    log.debug("SET PERIOD on SOURCE {} - {}".format(source, dev.write(
        "SOUR{}:FUNC:SQU:PER {}{}".format(source, period, period_unit))))
    time.sleep(delay)

print('hello')

def gen_duty_cycle(log, dev, source=1, dutycycle=50, delay=0):
    log.debug("SET DUTY CYCLE on SOURCE {} - {}".format(source,
                                                        dev.write("SOUR{}:FUNC:SQU:DCYC {}".format(source, dutycycle))))
    time.sleep(delay)


def gen_high_voltage(log, dev, source=1, vhigh=1, vhigh_unit="v", delay=0.15):
    log.debug("SET HIGH VOLTAGE on SOURCE {} - {}".format(source, dev.write(
        "SOUR{}:VOLT:HIGH {}{}".format(source, vhigh, vhigh_unit))))
    time.sleep(delay)


def gen_low_voltage(log, dev, source=1, vlow=0, vlow_unit="v", delay=0.15):
    log.debug("SET LOW VOLTAGE on SOURCE {} - {}".format(source, dev.write(
        "SOUR{}:VOLT:LOW {}{}".format(source, vlow, vlow_unit))))
    time.sleep(delay)


def set_gen_square(log, dev, source=1, dutycycle=50, period=1, period_unit="s", vhigh=1, vhigh_unit="v", vlow=0,
                   vlow_unit="v", delay=0.15):
    log.debug("SET UP GENERATOR SOURCE {} SQUARE SIGNAL PARAMETERS".format(source))
    log.debug("SET SQUARE on SOURCE {} - {}".format(source, dev.write("SOUR{}:FUNC SQU".format(source))))
    time.sleep(delay)

    gen_period(log, dev, source=source, period=period, period_unit=period_unit, delay=delay)

    gen_duty_cycle(log, dev, source=source, dutycycle=dutycycle, delay=delay)

    gen_high_voltage(log, dev, source=source, vhigh=vhigh, vhigh_unit=vhigh_unit, delay=delay)

    gen_low_voltage(log, dev, source=source, vlow=vlow, vlow_unit=vlow_unit, delay=delay)

    log.debug("DONE!!!")


def set_osc_ch(log, dev, channel=1, vpd=0.75, zero_level=0):
    log.debug("SETTING OSCILLOSCOPE CHANNEL {}".format(channel))
    delay = 0.1
    log.debug("SET OSC CH{} VOLTS PER DIV - {}".format(channel, dev.write(
        'CH{}:VOLTS {:.2f}'.format(channel, vpd))))  # VOLTS per div # 25 points per vertical div
    time.sleep(delay)
    log.debug("SET OSC CH{} ZERO LEVEL - {}".format(channel, dev.write(
        "CH{}:POS {}".format(channel, zero_level))))  # in DIVS not in volts
    time.sleep(delay)


def set_osc_hor(log, dev, t=10 ** -3):
    dev.write('HOR:MAIN:SCALE {:.9f}'.format(t))  # Sec per div # 250 points in horizontal div
    time.sleep(0.15)


def set_trigger(log, dev, channel=1, level=1.0):
    log.debug("TRIGGER SETUP")
    delay = 0.1
    log.debug("SET OSC TRIGGER SOURCE TO CH{} - {}".format(channel, dev.write(
        'TRIG:MAI:PUL:SOU CH{}'.format(channel))))
    time.sleep(delay)
    log.debug("SET TRIG LEVEL - {}".format(dev.write('TRIG:MAI:LEV {:.2f}'.format(level))))
    time.sleep(delay)


def start_gen(log, dev, source=1):
    log.debug("TURN GEN SOURCE{} ON - {}".format(source, dev.write('OUTP{} 1'.format(source))))
    time.sleep(0)


def stop_gen(log, dev, source=1):
    log.debug("TURN GEN SOURCE{} OFF - {}".format(source, dev.write('OUTP{} 0'.format(source))))
    time.sleep(0.15)


def osc_get_data(log, dev):
    """RETURS DATA IN STRING FORMAT"""
    log.debug("READ OSC DATA - {}".format(dev.write('ACQ:STATE ON')))  # record one snapshot
    time.sleep(0)
    # basically, screenshot

    # receive data and return as string of bytes
    data = dev.query_binary_values('CURV?', datatype='h', is_big_endian=True)
    # data = dev.query('CURV?')
    # data = data[13:-1:]
    return data

def set_gen_form(log, dev, func, freq = 0.1, amp=0.5, offset=0):
    log.debug("TURN GEN SOURCE{}".format(dev.write('APPLy:{} {}kHz,{},{}'.format(func,freq,amp,offset))))
    time.sleep(0)

def gen_reset(dev):
    dev.write('*RST')

def printer(s):
    print(s)

def uncoupling(l, dev, imp_time):
    gen_low_voltage(l, gen, source=1, vlow=-0.200, vlow_unit="v", delay=0)
    gen_high_voltage(l, gen, source=1, vhigh=-0.195, vhigh_unit="v", delay=0)
    gen_period(l, gen, source=1, period=1, period_unit="s", delay=0)
    gen_duty_cycle(l, gen, source=1, dutycycle=50, delay=0)
    # start_gen(l, gen,source=1)
    print("UNCOUPLING(-0.2V)...{} sec".format(imp_time))
    time.sleep(imp_time)
    # stop_gen(l, dev, source=1)
    print("UNCOUPLING DONE")

def coupling(l, dev, imp_time):
    # gen_low_voltage(l, gen, source=1, vlow=0.81, vlow_unit="v", delay=0)
    # gen_high_voltage(l, gen, source=1, vhigh=0.8, vhigh_unit="v", delay=0)
    # gen_period(l, gen, source=1, period=1, period_unit="s", delay=0)
    # gen_duty_cycle(l, gen, source=1, dutycycle=50, delay=0)
    # start_gen(l, gen,source=1)
    set_gen_form(l, gen, func='NOIS', freq=1, amp=0, offset=0.8)
    print("COUPLING(0.8V)...{} sec".format(imp_time))
    time.sleep(imp_time)
    # stop_gen(l, dev, source=1)
    print("COUPLING DONE")
def osc_reset(dev):
    dev.write("*RST")
def capture_data(l, dev, w_time, snap_period, f_name):
    result_time = []
    result = []

    start_time = dt.now().timestamp()
    temp = start_time
    print("START CAPTURING FOR {}sec AT {}".format(w_time, start_time))
    while temp-start_time < w_time:
        temp = dt.now().timestamp()
        result_time.append(temp-start_time)
        # print('capturing iter')
        result.append(osc_get_data(l, osc))
        while dt.now().timestamp()-temp < snap_period:
            pass

    with open(f_name, "w") as f:
        ret = [result, result_time]
        f.write(str(ret))
    print("WROTE DOWN TO FILE {}".format(f_name))

# def start_voltage_experiment(low_voltage = 0.15, high_voltage = 0.95, step = 0.1, dcycle = 50, impact_time = 5*60, snap_period = 0.5,
#                              func = "SQU"):
#     i = 0
#     result = []
#     result_time = []
#
#     while low_voltage+i*step < high_voltage:
#
#         uncoupling(l, gen)
#
#         gen_duty_cycle(log=l, dev=gen, source=1, dutycycle=dcycle, delay=0.15)
#         set_gen_form(l, gen, func=func, amp=(low_voltage+i*step)/2, offset=0)
#         start_gen(l, gen, source=1)
#         print("START GENERATING = {}V VOLTAGE".format(low_voltage+i*step))
#         # time.sleep(20)
#
#         start_time = dt.now().timestamp()
#         while temp-start_time < impact_time:
#             temp = dt.now().timestamp()
#             result_time.append(temp-start_time)
#             result.append(osc_get_data(l, gen))
#
#             while dt.now().timestamp()-temp < snap_period:
#                 pass
#
#         with open("mem_experiments/VOL_{}_FUNC_{}_IMPTIME(sec)_{}".format(i*step+low_voltage, func, impact_time), "w") as f:
#             ret = [result, result_time]
#             f.write(str(ret))
#
#         result_time = []
#         result = []
#
#         i+=1


#################################################################
vpd = 0.75
rez_coef = 25 // vpd  # 50

rm = visa.ResourceManager()
rm.list_resources("?*")
gen = rm.open_resource("USB0::0x4348::0x5537::NI-VISA-30002::RAW")
gen.timeout = 5000
osc = rm.open_resource("USB0::0x0699::0x03A6::C041256::INSTR")
print(osc)
osc.timeout = 5000
set_osc_ch(l, osc, 1, 0.6, 0)
# set_osc_hor(l, osc, t=10 ** -3)
osc.encoding = "utf-8"
osc.query("*IDN?")
osc.write("DATa:ENCdg RIBinary")
osc.write("DATa:WIDth 2")


# main

step = 0.1
i=0
offset = 0.15

min_voltage = 0.3
max_voltage = 0.1

min_freq = 0.02
max_freq = 0.52

min_dcycle = 20
max_dcycle = 80
###
# gen_duty_cycle(l, gen, source=1, dutycycle=50, delay=0.15)
# set_gen_form(l, gen, "SQU", freq = 0.1, amp=0.5, offset=0)
# start_gen(l, gen,source=1)

# uncoupling(l, gen, 10)
# os.remove("test_papk")
# os.mkdir("test_papk")
# capture_data(l, osc, w_time=10, snap_period=0.5, f_name="test_papk/hello.txt")
###
gen_reset(gen)

stop_gen(l, gen, source=1)

voltages = [-0.2, 0]
dcycles = [80, 60, 30, 10]
freqs = [0.02, 0.1, 0.2, 0.5]
osc_hors = [10*10**-3, 2.5*10**-3, 1*10**-3, 0.5*10**-3]

set_gen_form(l, gen, func="NOIS", freq=1, amp=0, offset=0.15)
start_gen(l, gen, source=1)
print("Starting experiment cycle. Switch on the supply and plug in the memristor. Waiting 50sec...")
time.sleep(50)
curr = min_voltage
step = 0.1
counter = 0
for curr in freqs:
    set_osc_hor(l, osc, osc_hors[counter])
    counter+=1
    coupling(l, gen, 5*60)
    # print(curr)
    gen_duty_cycle(l, gen, source=1, dutycycle=10, delay=0)
    set_gen_form(l, gen, func="REXP", freq=curr, amp=abs(-0.2-0.15), offset=(-0.2- 0.15) / 2 + 0.15 - 0.008)
    start_gen(l, gen, source=1)
    print("GENERATING {}".format(curr))

    capture_data(l, osc, w_time=5*60, snap_period=0.5, f_name="freq_{}.txt".format(
        curr))
    # time.sleep(15)
    # start_gen(l, gen, source=1)
    # curr+=step

print('cycle done')
set_gen_form(l, gen, func="NOIS", freq=1, amp=0, offset=0.15)
start_gen(l, gen, source=1)
print("EXPERIMENT DONE. Plug off the memristor and switch off the supply.")
time.sleep(50)

# stop_gen(l, gen, source=1)

input('done')