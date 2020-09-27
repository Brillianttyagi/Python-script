#!/usr/bin/env python
import psutil
cpu_usage = psutil.cpu_percent()
print(cpu_usage)