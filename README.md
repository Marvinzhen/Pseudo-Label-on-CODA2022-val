# Pseudo-Label-on-CODA2022-val
Llava-based pseudo label creation and labelme based adjustment
## 用LLava大语言模型初步创建伪标签
### 整理输入问题文件
'
python generate_q.py
'
### 初步创建伪标签基于LLava大模型实现，[LLava代码](https://github.com/haotian-liu/LLaVA?tab=readme-ov-file)，在模型下添加model_vqa1.py运行。
'
python model_vqa1.py \
    --model-path ./checkpoints/LLaVA-13B-v0 \
    --question-file \
    playground/data/coco2014_val_qa_eval/qa90_questions.jsonl \
    --image-folder \
    /path/to/coco2014_val \
    --answers-file \
    /path/to/answer-file-our.jsonl
'
## 用labelme调整伪标签
### labelme下载
'
conda create --name=labelme python=3.6
conda activate labelme
pip install pyqt5
pip install labelme
'
### 整理初步输出的伪标签，对应为labelme可接受格式
'
python label.py
'
### 使用labelme调整
'
labelme path/to/images --output path/to/output --flags xxx.txt --nodata
'
