from collections import defaultdict

def read_population_data(file_path):
    """Зчитує дані з файлу та повертає список словників."""
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.strip():
                continue
            country, year, pop = line.strip().split(',')
            data.append({
                'country': country.strip(),
                'year': int(year.strip()),
                'population': int(pop.strip())
            })
    return data

def calculate_population_change(data):
    """Розраховує зміну населення за роками для кожної країни."""
    data_sorted = sorted(data, key=lambda x: (x['country'], x['year']))
    
    country_groups = defaultdict(list)
    for item in data_sorted:
        country_groups[item['country']].append(item)
        
    changes = {}
    for country, records in country_groups.items():
        country_changes = {}
        for i in range(1, len(records)):
            prev = records[i-1]
            curr = records[i]
            change = curr['population'] - prev['population']
            period_key = f"{prev['year']}-{curr['year']}"
            country_changes[period_key] = change
        changes[country] = country_changes
        
    return changes