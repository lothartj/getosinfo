import platform
import getpass
import os
import socket
import psutil
import datetime
import subprocess
import sys
import time
import pyautogui
from django.shortcuts import render

def getosinfo(request):
    # Get the username of the currently logged-in user and capitalize it
    username = getpass.getuser().capitalize()

    # Get system platform information
    system_platform = platform.platform()

    # Get machine network name
    machine_network_name = socket.gethostname()

    # Get machine IP address
    machine_ip_address = socket.gethostbyname(machine_network_name)

    # Get operating system name
    operating_system_name = os.name

    # Get number of CPU cores
    num_cpu_cores = os.cpu_count()

    # Get total memory (RAM) and round it off
    total_memory = round(psutil.virtual_memory().total / (1024 ** 3), 2)

    # Get available memory (RAM)
    available_memory = round(psutil.virtual_memory().available / (1024 ** 3), 2)

    # Get total disk space
    total_disk_space = round(psutil.disk_usage('/').total / (1024 ** 3), 2)

    # Get available disk space in GB with decimals
    available_disk_space = round(psutil.disk_usage('/').free / (1024 ** 3), 2)

    # Calculate system uptime and format it
    def format_uptime(uptime):
        uptime_seconds = uptime - psutil.boot_time()
        uptime_timedelta = datetime.timedelta(seconds=uptime_seconds)
        days = uptime_timedelta.days
        hours, remainder = divmod(uptime_timedelta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"

    system_uptime = format_uptime(psutil.boot_time())

    # Get battery percentage
    battery_percentage = psutil.sensors_battery().percent

    # Get battery power status
    battery_sensors = psutil.sensors_battery()
    battery_power_status = "Plugged" if battery_sensors and battery_sensors.power_plugged else "Unplugged"

    # Get list of running processes
    running_processes = [process.name() for process in psutil.process_iter()]

    # Get current user logged in
    current_user = os.getlogin().capitalize()

    # Get list of mounted filesystems
    mounted_filesystems = psutil.disk_partitions()

    # Get system hostname
    system_hostname = socket.gethostname()

    # Get MAC addresses of network interfaces
    network_interfaces = psutil.net_if_addrs()

    open_ports = []

    if request.method == 'POST':
        host = request.POST.get('host')
        start_port = int(request.POST.get('start_port'))
        end_port = int(request.POST.get('end_port'))

        for port in range(start_port, end_port + 1):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(0.5)  # Set timeout for socket connection
                    s.connect((host, port))
                open_ports.append(port)
            except (socket.timeout, ConnectionRefusedError):
                pass

    # Get system DNS resolver configuration
    dns_resolver_config = socket.getaddrinfo('www.example.com', 80)

    # Get system kernel version
    kernel_version = platform.release()

    # Get system architecture
    architecture = platform.architecture()

    # Get Python version
    python_version = sys.version

    # Get total number of logical CPUs
    logical_cpus = os.cpu_count()

    # Get the system's root directory
    system_root_directory = os.path.abspath('/')

    # Get the current system boot time
    boot_time = round(psutil.boot_time(), 2)

    # Get the current system boot time
    boot_time = psutil.boot_time()
    # Get the current time
    current_time = time.time()
    # Calculate the uptime (time since last restart) in seconds
    uptime = current_time - boot_time

    # Get the number of users currently logged in
    num_logged_in_users = len(psutil.users())

    # Get the number of running processes
    num_running_processes = len(psutil.pids())

    # Get the current screen resolution
    screen_resolution = pyautogui.size()

    import subprocess

    def get_windows_firewall_configuration():
        try:
            result = subprocess.run(['netsh', 'advfirewall', 'show', 'allprofiles'], capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            return f"Error: {e}"

    # Example usage
    if __name__ == "__main__":
        firewall_info = get_windows_firewall_configuration()

    # Create a context dictionary with all the information
    context = {
        'username': username,
        'system_platform': system_platform,
        'machine_network_name': machine_network_name,
        'machine_ip_address': machine_ip_address,
        'operating_system_name': operating_system_name,
        'num_cpu_cores': num_cpu_cores,
        'total_memory': total_memory,
        'available_memory': available_memory,
        'total_disk_space': total_disk_space,
        'available_disk_space': available_disk_space,
        'system_uptime': system_uptime,
        'battery_percentage': battery_percentage,
        'battery_power_status': battery_power_status,
        'running_processes': running_processes,
        'current_user': current_user,
        'mounted_filesystems': mounted_filesystems,
        'system_hostname': system_hostname,
        'network_interfaces': network_interfaces,
        'open_ports': open_ports,
        'dns_resolver_config': dns_resolver_config,
        'kernel_version': kernel_version,
        'architecture': architecture,
        'python_version': python_version,
        'logical_cpus': logical_cpus,
        'system_root_directory': system_root_directory,
        'boot_time': boot_time,
        'uptime': uptime,
        'num_logged_in_users': num_logged_in_users,
        'num_running_processes': num_running_processes,
        'screen_resolution': screen_resolution,

    }

    # Pass the context to the template for rendering
    return render(request, "index.html", context)
