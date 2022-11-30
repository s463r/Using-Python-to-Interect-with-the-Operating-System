#!/usr/bin/env python3
import psutil
import shutil

def disk_usage():
	du = shutil.disk_usage("/")
	free_space = du.free / du.total * 100
	return [free_space > 20, free_space]

def disk_usage_am():
	du = shutil.disk_usage("/")
	free_space = du.free / du.total * 100
	return free_space

def cpu_usage():
	return psutil.cpu_percent(1) < 75

if not disk_usage()[0] or not cpu_usage():
	print("##### CAUTION! #####")
	if not disk_usage()[0]:
		print(f"Free space is {disk_usage()[1]:.2f} %. Disk Space is Critically Low")
	elif not cpu_usage():
		print(f"Free space is {cpu_usage()} %. CPU Space is Critically Low")
else:
	print("Everything is OK!")