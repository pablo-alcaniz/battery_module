#!/bin/bash
cpupower frequency-set -g performance
echo "· CPU governor set to: PERFORMANCE" >> /bin/battery_module/log_battery_module