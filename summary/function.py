def transform_data(input_data):
    transformed_data = {
        'load': int(next(item['summary'] for item in input_data if item['name'] == 'Load')),
        'schedule': int(next(item['summary'] for item in input_data if item['name'] == 'Schedule')),
        'drawl': int(next(item['summary'] for item in input_data if item['name'] == 'Drawl')),
        'currentRevision': next(item['summary'] for item in input_data if item['name'] == 'Current Revision'),
        'maxLoadToday': next(item['summary'] for item in input_data if item['name'] == 'Max Load Today'),
        'maxLoadYesterday': next(item['summary'] for item in input_data if item['name'] == 'Max Load Yesterday'),
        'frequency': float(next(item['summary'] for item in input_data if item['name'] == 'Frequency')),
        'uiRate': int(next(item['summary'] for item in input_data if item['name'] == 'UI Rate')),
        'od/ud': int(next(item['summary'] for item in input_data if item['name'] == 'Od')),
        'delhiGeneration': int(next(item['summary'] for item in input_data if item['name'] == 'Delhi Generation')),
        'minLoadToday': next(item['summary'] for item in input_data if item['name'] == 'Minimum Load Today'),
        'minLoadYesterday': next(item['summary'] for item in input_data if item['name'] == 'Minimum Load Yesteday')
    }

    return transformed_data
