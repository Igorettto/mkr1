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