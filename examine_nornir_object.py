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

#Failed tasks
results.failed_hosts['csr10'].result

#Copy data to new object
results2 = results.copy()

nxos1=results['nxos1'].copy()
nxos1
nxos1[0].result


def extract_nornir_mul_result(agg_result):
    '''
    nornir aggresult is all returns of all data
    nornir mul_result is all the returns of a specific host/task
    nornir result is the single return of a single host/task
    '''
    for host, task_result in agg_result.items():
        mul_result = agg_result[host]
        return mul_result


def extract_nornir_result(agg_result):
    '''
    nornir aggresult is all returns of all data
    nornir mul_result is all the returns of a specific host/task
    nornir result is the single return of a single host/task
    '''
    for host, task_result in agg_result.items():
        mul_result = agg_result[host]
        result = mul_result[0]
        return result
