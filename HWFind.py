import psutil
import platform
import cpuinfo

uname = platform.uname()
cpuFreq = psutil.cpu_freq()
cpuInfo = cpuinfo.get_cpu_info()
print(f"OS: {uname.system} {uname.release} ({uname.version})")
print(f"Host: {uname.node}")
print(f"Processor: {cpuInfo['brand_raw']}")
print(f"Cores: {psutil.cpu_count(logical=False)} Cores {psutil.cpu_count(logical=True)} Threads")
mem = psutil.virtual_memory()
currentMem = mem.used / (1024 ** 3)  # Convert to GB
totalMem = mem.total / (1024 ** 3)    # Convert to GB
print(f"Memory: {currentMem:.2f}/{totalMem:.2f} GB")