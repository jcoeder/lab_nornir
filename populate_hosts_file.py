"""
Script to gather facts from the NAPALM compatible devices
in inventory and that new information to the inventory
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
import yaml


#Disable SSL Warnings
urllib3.disable_warnings()


def main():
    # Init the Nornir object
    nr = InitNornir(config_file="config.yaml")
    
    # Filter out only NAPALM compatible devices
    nr = nr.filter(F(platform='nxos') | F(platform='ios') | F(platform='junos') | F(platform = 'eos'))
    
    # Save AggResult to a variable
    results = nr.run(task=napalm_get, getters=['facts'])
    
    # Open existings hosts file and load it into a dictionary
    with open('inventory/hosts.yaml') as f:
        hosts_dict = yaml.safe_load(f)
    # Create the data key    
    for key in hosts_dict.keys():
        hosts_dict[key]['data'] = {}

    # For each key/value - host/multiresult
    for host, multiresult in results.items():
        # Extract the result from the multiresult
        result = multiresult[0].result
        try:
            # Add extracted information as keys to the dictionary
            hosts_dict[host]['data']['hostname'] = result['facts']['hostname']
            hosts_dict[host]['data']['model'] = result['facts']['model']
            hosts_dict[host]['data']['serial_number'] = result['facts']['serial_number']
        except TypeError:
            # If host fails to return data get_result will be an empty dictionary.
            pass

    # Write new dictionary to YAML file
    with open('inventory/hosts.yaml', 'w') as f:
        yaml.dump(hosts_dict, f, default_flow_style=False)


if __name__ == "__main__":
    main()
