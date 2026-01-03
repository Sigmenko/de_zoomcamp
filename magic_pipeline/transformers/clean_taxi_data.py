if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@transformer
def transform(data, *args, **kwargs):
    print(f"Rows before cleaning: {len(data)}")

    data = data[data['passenger_count'] > 0]
    # Залишаємо тільки де проїхали більше 0 км
    data = data[data['trip_distance'] > 0]

    data['price_for_km'] = data['total_amount'] / data['trip_distance']

    data = data[data['total_amount'] < 500]
    print(f"Rows after cleaning: {len(data)}")

    return data

@test
def test_output(output, *args) -> None:
    # Перевірка (тест): чи точно не залишилось нульових пасажирів?
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are rides with 0 passengers'