import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    try:
        data = []
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)
                
        with open(json_file_path, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
            
        print(f"CSV file '{csv_file_path}' has been converted to JSON file '{json_file_path}' successfully.")
                        
    except FileNotFoundError:
        print(f"Error: The file '{csv_file_path}' does not exist.")
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from the file '{json_file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    csv_to_json('student.csv', 'student.JSON')                                                                                                                                     
                    
                    
