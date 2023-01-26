#!/bin/bash
cpupower frequency-set -g powersave
echo "· CPU governor set to: POWERSAVE" >> /bin/battery_module/log_battery_module