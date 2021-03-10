import json


def save_entry(new_data_dict):
    data = {}
    try:
        with open("data.json", "r") as data_file:
            # Read old data
            data = json.load(data_file)
    except FileNotFoundError or json.decoder.JSONDecodeError:
        data = new_data_dict
    else:
        # Update old data with new data
        data.update(new_data_dict)
    finally:
        with open("data.json", "w") as data_file:
            # Save updated data
            json.dump(data, data_file, indent=4)
