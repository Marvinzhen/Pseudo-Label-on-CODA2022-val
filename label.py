import json
import os

def process_answer_jsonl(input_file):
    output_folder = "CODA2022-val/output"
    os.makedirs(output_folder, exist_ok=True)

    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for index, line in enumerate(lines):
        data = json.loads(line)
        type_info = data["text"].split("Type: ")[1].split("; Reason")[0].strip()

        # Create the output JSON data
        output_data = {
            "version": "5.0.2",
            "flags": {
                "littering": False,
                "traffic accidents": False,
                "construction": False,
                "parking violations": False,
                "intrusion of non-motorized vehicles": False,
                "pedestrian violations": False,
                "obstacles": False,
                "traffic facility issues": False,
                "normal": False,
                "traffic congestion": False,
                "traffic": False
            },
            "shapes": [],
            "imagePath": f"..\\images\\{index + 1:04d}.jpg",  # Assuming images are named like 0001.jpg, 0002.jpg, etc.
            "imageData": None,
            "imageHeight": 720,
            "imageWidth": 1355
        }

        # Update the flags based on the type_info
        if type_info.lower() in output_data["flags"]:
            output_data["flags"][type_info.lower()] = True
        else:
            print(f"Warning: Unknown type '{type_info}' in line {index + 1}")

        # Save the output JSON to a file
        output_filename = os.path.join(output_folder, f"{index + 1:04d}.json")
        with open(output_filename, "w", encoding="utf-8") as out_file:
            json.dump(output_data, out_file, indent=2)

if __name__ == "__main__":
    input_jsonl_file = "answer.jsonl"
    process_answer_jsonl(input_jsonl_file)
