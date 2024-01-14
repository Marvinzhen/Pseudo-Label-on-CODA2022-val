import os
from PIL import Image
import json

# 输入文件夹路径
input_folder = '/mnt/data3/v2x_project/LLaVA/playground/coda/images'

# 输出JSONL文件路径
output_jsonl_path = 'question.jsonl'

# 遍历文件夹中的所有图片文件
for idx, filename in enumerate(sorted(os.listdir(input_folder))):
    if filename.endswith(".jpg"):
        image_path = os.path.join(input_folder, filename)

        # 读取图像信息
        with Image.open(image_path) as img:
            width, height = img.size

        # 构造问题信息字典
        question_info = {
            "question_id": idx,
            "image": filename,
            "text": "Given the following image of a traffic scene, please analyze and provide the following format of response: Type: [one of the candidate types, e.g., littering, traffic accidents, construction, parking violations, intrusion of non-motorized vehicles, pedestrian violations, obstacles, traffic facility issues]; Reason: [concise phrase explaining the identified issue ]. If no specific corner cases are identified, respond with: Type: normal; Reason: No corner cases found.",
            "category": "detail"
        }

        # 将问题信息字典写入JSONL文件
        with open(output_jsonl_path, 'a') as jsonl_file:
            jsonl_file.write(json.dumps(question_info) + '\n')

print(f"JSONL文件已创建：{output_jsonl_path}")



