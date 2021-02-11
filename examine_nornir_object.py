'''
Tearing apart the nornir object
'''
print(results) # dictionary like object of all returned data
print(results.items()) # dictionary items of returned data with hostnames as keys - recuresses the whole inventory structue, not just single host or group
print(results['nxos1']) # dictionary like object of returned data for single host
print(results['nxos1'].result) # dictionary of all returned information with individual getters as keys
print(results['nxos1'].result['config']) # dive into dictionary
print(results['nxos1'].result['config']['running']) # dive into dictionary
print(results['nxos1'].result['facts']) # dive into dictionary
print(results['nxos1'].result['facts']['serial']) # dive into dictionary
print(results['nxos1'].result['facts']['serial_number']) # dive into dictionary
