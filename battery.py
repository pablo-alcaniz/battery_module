import time
import subprocess

time_sleep = 0.5
cont = True
last_status = 1

g = open('/sys/class/power_supply/ADP1/online')
status_ini = int(g.read(1))

if status_ini == 1:
    subprocess.call("/bin/battery_module/log_ac.sh")
    subprocess.call("/bin/battery_module/backlight_ac.sh")
    subprocess.call("/bin/battery_module/epb_ac.sh")
    subprocess.call("/bin/battery_module/governor_batt.sh")
    subprocess.call("/bin/battery_module/turbo_boost_ac.sh")
    subprocess.call("/bin/battery_module/freq_ac.sh")
    last_status = 1
elif status_ini == 0:
    subprocess.call("/bin/battery_module/log_batt.sh")
    subprocess.call("/bin/battery_module/backlight_batt.sh")
    subprocess.call("/bin/battery_module/epb_batt.sh")
    subprocess.call("/bin/battery_module/governor_batt.sh")
    subprocess.call("/bin/battery_module/turbo_boost_batt.sh")
    subprocess.call("/bin/battery_module/freq_batt.sh")
    last_status = 0

while True:
    f = open('/sys/class/power_supply/ADP1/online')
    status = int(f.read(1))

    if last_status == status:
        time.sleep(time_sleep)
        continue
    else:
        if status == 1:
            subprocess.call("/bin/battery_module/log_ac.sh")
            subprocess.call("/bin/battery_module/backlight_ac.sh")
            subprocess.call("/bin/battery_module/epb_ac.sh")
            subprocess.call("/bin/battery_module/governor_batt.sh")
            subprocess.call("/bin/battery_module/turbo_boost_ac.sh")
            subprocess.call("/bin/battery_module/freq_ac.sh")
            last_status = 1
            time.sleep(time_sleep)
        elif status == 0:
            subprocess.call("/bin/battery_module/log_batt.sh")
            subprocess.call("/bin/battery_module/backlight_batt.sh")
            subprocess.call("/bin/battery_module/epb_batt.sh")
            subprocess.call("/bin/battery_module/governor_batt.sh")
            subprocess.call("/bin/battery_module/turbo_boost_batt.sh")
            subprocess.call("/bin/battery_module/freq_batt.sh")
            last_status = 0
            time.sleep(time_sleep)
        else:
            time.sleep(time_sleep)
            continue
