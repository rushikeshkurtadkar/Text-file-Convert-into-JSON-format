import json

def convert_chat_to_json(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    chat_data = []
    for line in lines:
        if ": " in line:
            sender, message = line.strip().split(": ", 1)
            chat_data.append({"sender": sender, "message": message})

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(chat_data, file, indent=4, ensure_ascii=False)

    print(f"✅ JSON file saved: {output_file}")

# ✅ Fix the path issue
input_cleaned_chat = r"C:\Users\rushi\Downloads\project\wa\cleaned_chat_WA.txt"
output_json_file = r"C:\Users\rushi\Downloads\project\wa\chat_data.json"

convert_chat_to_json(input_cleaned_chat, output_json_file)
