# https://codechalleng.es/bites/promo/datastructures

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps():
    # return cars['Jeep']
    return ', '.join(cars['Jeep'])


def get_first_model_each_manufacturer():
    """return a list of matching models (original ordering)"""
    """items = []
    for car in cars:
        items.append(cars[car][0])
    return items"""

    return [models[0] for models in cars.values()]


def get_all_matching_models(grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    grep = grep.lower()
    models = sum(cars.values(), [])  # flatten list of lists
    matching_models = [model for model in models
                       if grep in model.lower()]
    return sorted(matching_models)


def sort_car_models():
    """sort the car models (values) and return the resulting cars dict"""
    return {manufacturer: sorted(models) for
            manufacturer, models in cars.items()}

print(get_all_jeeps())
print(get_first_model_each_manufacturer())
print(get_all_matching_models(grep='CO'))
print(sort_car_models())