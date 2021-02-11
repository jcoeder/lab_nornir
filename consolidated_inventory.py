"""
Script to gather facts from the NAPALM compatible devices
in inventory and print that information to the screen
for each device.
"""

__author__ = "Justin Oeder"
__version__ = "0.0.1"
__license__ = "MIT"


from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result
from nornir.core.filter import F
import sys
import urllib3


#Disable SSL Warnings
urllib3.disable_warnings()


def main():
    # Init the Nornir object
    nr = InitNornir(config_file="config.yaml")
    
    # Filter out only NAPALM compatible devices
    nr = nr.filter(F(platform='nxos') | F(platform='ios') | F(platform='junos') | F(platform = 'eos'))
    
    # Save AggResult to a variable
    results = nr.run(task=napalm_get, getters=['facts'])
    
    # For each key/value - host/multiresult
    for host, multiresult in results.items():
        # Extract the result from the multiresult
        result = multiresult[0].result
        try:
            print(result['facts']['hostname'])
            print(result['facts']['model'])
            print(result['facts']['serial_number'])
            print('')
        except TypeError:
            # If host fails to return data get_result will be an empty dictionary.
            print('Host ' + host + ' failed!  Check the log file.')
            print('')        


if __name__ == "__main__":
    main()
