import json

def analyze_json_data(json_data):
    # Load JSON data into a Python data structure
    try:
        data = json.loads(json_data)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return

    # Perform analysis on the JSON data
    if isinstance(data, dict):
        print("JSON data is a dictionary.")
        print("Keys:", data.keys())
        print("Values:", data.values())
    elif isinstance(data, list):
        print("JSON data is a list.")
        print("Number of elements:", len(data))
        print("Elements:", data)
    else:
        print("Unsupported JSON data type.")

if __name__ == "__main__":
    # Example JSON data
    json_data = '''
    {
        "name": "John Doe",
        "age": 30,
        "city": "New York",
        "skills": ["Python", "Java", "JavaScript"],
        "is_student": false
    }
    '''

    # Analyze the JSON data
    analyze_json_data(json_data)
