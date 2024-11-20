def validate_input(input_data, category):
    valid_categories = ["race", "class", "customization"]
    return category in valid_categories and isinstance(input_data, str)
