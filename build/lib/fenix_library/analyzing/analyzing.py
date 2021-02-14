# FENIX INSTALLER
# Please refer to the file `LICENSE` in the main directory for license information. 
# For a high level documentation, please visit https://gitlab.com/rebornos-team/fenix-installer

# AUTHORS
# 1. Shivanand Pattanshetti (shivanand.pattanshetti@gmail.com)
# 2. 

# IMPORTS
from __future__ import annotations
import psutil
import urllib.request 
import urllib.error
import platform
import pathlib
import functools
from typing import Dict, List, Any, Optional, Union

# FENIX IMPORTS
from fenix_library.running import BatchJob, LogMessage, Function, Command, LoggingHandler
from fenix_library.configuration import JSONConfiguration

class SystemAnalyzer(BatchJob):
    """
    Handy tools to analyze the host system. Based on using the library `psutil`

    TODO
    ----
    - Power
        - Plugged in or not
        - Battery percentage
    - Storage
        - Devices
        - Free space
        - Used space
        - UUID
        - Total
        - label
    - Network connection
    - GPU
    - Boot mode
    - System architecture
    """

    # CONSTRUCTOR
    def __init__(
        self,
        thread_name:str= "SystemAnalysisJob",
        logging_handler: Optional[LoggingHandler] = None,
        pre_run_function: Optional[functools.partial] = None,
        post_run_function: Optional[functools.partial] = None
    ) -> None:
        """
        Initialize a 'SystemAnalyzer' object
        
        Parameters
        ----------
        thread_name: str, default "SystemAnalysisJob"
            Name for prefixing the threads
        logging_handler: Optional[LoggingHandler]
            The LoggingHandler object which stores the logging functions, logging threads, logger information, etc.
        pre_run_function: functools.partial, default None
            A function to be called before the installation starts. Its name and arguments are wrapped together by calling functools.partial
        post_run_function: functools.partial, default None
            A function to be called after the installation finishes. Its name and arguments are wrapped together by calling functools.partial
        """

        self.system_configuration: JSONConfiguration = JSONConfiguration("configuration/system.json")

        # Call the parent class constructor
        super().__init__(
            thread_name= thread_name,
            logging_handler= logging_handler,
            pre_run_function= pre_run_function,
            post_run_function= post_run_function
        )
           
    # REGULAR METHODS

    def start(self) -> None:
        """
        Start analyzing the system by running self._boss() on a separate thread

        Parameters
        ----------
        None

        Returns
        -------
        Nothing
        """

        self._queue_analysis()
        super().start()
        
    def do_power_analysis(self) -> None:
        """
        Check if the host system is plugged in and has enough charge if on battery

        Parameters
        ----------
        None

        Returns
        -------
        Nothing
        """
        
        battery_status: Optional[psutil._common.sbattery] = psutil.sensors_battery()
        self.system_configuration["power"]["plugged_in"] = battery_status.power_plugged
        self.system_configuration["power"]["charge"] = battery_status.percent

    def do_storage_analysis(self) -> None:
        """
        Analyze the host system's storage

        Parameters
        ----------
        None

        Returns
        -------
        Nothing
        """
        
        partition_statuses: List[psutil._common.sdiskpart] = psutil.disk_partitions(all= True)
        partitions: Dict[str, Dict[str, Any]] = {}
        for partition_status in partition_statuses:
            if partition_status.device.startswith("/dev/sd"):
                disk_usage_status = psutil.disk_usage(partition_status.mountpoint)
                partitions[partition_status.device] = {
                    "mountpoint": partition_status.mountpoint,
                    "filesystem_type": partition_status.fstype,
                    "mount_options": partition_status.opts,
                    "free_space": disk_usage_status.free,
                    "used_space": disk_usage_status.used,
                    "total_space": disk_usage_status.total,
                    "percentage_used": disk_usage_status.percent
            }
        self.system_configuration["storage"]["partitions"] = partitions

    def do_network_analysis(self) -> None:
        """
        Check if the host system has internet connectivity

        Parameters
        ----------
        None

        Returns
        -------
        Nothing
        """

        try:
            urllib.request.urlopen("https://google.com", timeout=5)
            self.system_configuration["internet"]["connected"] = True
        except urllib.error.URLError:
            self.system_configuration["internet"]["connected"] = False

    def do_architecture_analysis(self) -> None:
        """
        Check the host system's architecture

        Parameters
        ----------
        None

        Returns
        -------
        Nothing
        """

        self.system_configuration["architecture"] = platform.machine()

    def do_boot_mode_analysis(self) -> None:
        """
        Check the host system's boot mode

        Parameters
        ----------
        None

        Returns
        -------
        Nothing
        """

        efi_path = pathlib.Path("/sys/firmware/efi/efivars")
        if efi_path.exists() and efi_path.is_dir():
            self.system_configuration["boot_mode"] = "uefi"
        else:
            self.system_configuration["boot_mode"] = "bios"

    def do_GPU_analysis(self) -> None:
        """
        Check the host system's GPU

        Parameters
        ----------
        None

        Returns
        -------
        Nothing
        """

        # Old syntax: The Python way
        # lspci_process = subprocess.Popen(
        #     ["lspci", "-k"],
        #     stdout=subprocess.PIPE,
        #     universal_newlines= False
        # )
        # grep_process = subprocess.Popen(
        #     ["grep", "-E", "(VGA|3D)"],
        #     stdin=lspci_process.stdout,
        #     stdout=subprocess.PIPE,
        #     stderr=subprocess.PIPE,
        #     universal_newlines= False
        # )
        # grep_output = grep_process.communicate()[0].decode()
        command = Command(["lspci", "-k"]) | Command(["grep", "-E", "(VGA|3D)"])
        grep_output = command.run_and_wait()
        
        self.system_configuration["gpu"]["nvidia"] = False
        self.system_configuration["gpu"]["intel"] = False
        self.system_configuration["gpu"]["amd"] = False
        self.system_configuration["gpu"]["ati"] = False
        self.system_configuration["gpu"]["optimus"] = False
        if "NVIDIA" in grep_output:
            self.system_configuration["gpu"]["nvidia"] = True
        if "Intel" in grep_output:
            self.system_configuration["gpu"]["intel"] = True
        if "AMD" in grep_output:
            self.system_configuration["gpu"]["amd"] = True
        if "ATI" in grep_output:
            self.system_configuration["gpu"]["ati"] = True
        if self.system_configuration["gpu"]["nvidia"] is True and self.system_configuration["gpu"]["intel"] is True:
            self.system_configuration["gpu"]["optimus"] = True

    # PRIVATE METHODS

    def _queue_analysis(self) -> None:
        """
        Plan and queue the system analysis

        Parameters
        ----------
        None

        Returns
        -------
        Nothing
        """

        self += LogMessage.Info(message= "Analyzing the host system...")

        # Power 
        self += LogMessage.Info("Checking the power status...")
        self += Function(self.do_power_analysis)

        # Storage information
        self += LogMessage.Info("Analyzing storage...")
        self += Function(self.do_storage_analysis)

        # Network 
        self += LogMessage.Info("Checking internet connectivity...")
        self += Function(self.do_network_analysis)

        # System architecture
        self += LogMessage.Info("Determining the system architecture...")
        self += Function(self.do_architecture_analysis)

        # Boot mode
        self += LogMessage.Info("Checking the boot mode...")
        self += Function(self.do_boot_mode_analysis)

        # GPU information
        self += LogMessage.Info("Checking GPUs...")
        self += Function(self.do_GPU_analysis)

        # Write changes to the configuration files
        self += Function(self.system_configuration.write_data)

        # Notify completion
        self += LogMessage.Info(message= "Host system analysis complete...")

    # OVERLOADED OPERATORS

    # Usage examples: 
    # `system_analyzer_job += Command(["echo", "Hello"])`
    # `system_analyzer_job += Function(print, "Hello")`
    # `system_analyzer_job += LogMessage.Info("Hello")`
    # `system_analyzer_job += batch_job`
    # `system_analyzer_job += system_analyzer_job2`
    def __iadd__(
        self,
        other: Union[Command, Function, LogMessage, BatchJob, SystemAnalyzer]
    ) -> SystemAnalyzer:
        """
        Overloads the += operator to add tasks to the queue
        # Usage examples: 
        `system_analyzer_job += Command(["echo", "Hello"])`
        `system_analyzer_job += Function(print, "Hello")`
        `system_analyzer_job += LogMessage.Info("Hello")`
        `system_analyzer_job += batch_job`
        `system_analyzer_job += system_analyzer_job2`

        Parameters
        ----------
        other : Union[Command, Function, LogMessage, BatchJob]
            The second operand

        Returns
        -------
        BatchJob
            The modified BatchJob instance with the new task in queue
        """

        _ = super().__iadd__(other)
        return self