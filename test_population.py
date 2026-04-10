import pytest
from population import read_population_data, calculate_population_change

@pytest.fixture
def sample_txt_file(tmp_path):
    """Створює тимчасовий текстовий файл із тестовими даними"""
    file_content = "Ukraine, 2020, 41000000\nUkraine, 2021, 40500000\nPoland, 2020, 38000000\nPoland, 2021, 37900000"
    file_path = tmp_path / "test_data.txt"
    file_path.write_text(file_content, encoding='utf-8')
    return file_path

@pytest.fixture
def parsed_data():
    """Повертає вже розпарсені дані для тестування"""
    return [
        {'country': 'A', 'year': 2000, 'population': 100},
        {'country': 'A', 'year': 2001, 'population': 120},
        {'country': 'B', 'year': 2000, 'population': 50},
        {'country': 'B', 'year': 2001, 'population': 40},
    ]

def test_read_population_data(sample_txt_file):
    data = read_population_data(sample_txt_file)
    assert len(data) == 4
    assert data[0]['country'] == 'Ukraine'
    assert data[1]['year'] == 2021
    assert data[2]['country'] == 'Poland'
    assert data[3]['year'] == 2021

@pytest.mark.parametrize("country, period, expected_change", [
    ('A', '2000-2001', 20),
    ('B', '2000-2001', -10),
])
def test_calculate_population_data(parsed_data, country, period, expected_change):
    changes = calculate_population_change(parsed_data)
    assert changes[country][period] == expected_change