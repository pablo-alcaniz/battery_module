#!/bin/bash
cpupower frequency-set --max 2000000
cpupower frequency-set --min 800000
echo "· Max freq set to: 2.0 GHz" >> /bin/battery_module/log_battery_module
echo "· Min freq set to: 0.8 GHz" >> /bin/battery_module/log_battery_module