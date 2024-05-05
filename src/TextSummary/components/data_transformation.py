import os
from TextSummary.logging import logger
from TextSummary.entity import DataTransformationConfig
from datasets import load_dataset, load_from_disk
from transformers import T5Tokenizer


class Data_transformation:
    def __init__(self,config: DataTransformationConfig):
        self.config = config
        self.tokenizer =  T5Tokenizer.from_pretrained(config.tokenizer_name)

    
    def convert_data_to_features(self,example_batch):
        input_encodings = self.tokenizer(example_batch['dialogue'], max_length=1024, truncation = True, padding='max_length')

        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['summary'], max_length=128, truncation = True, padding='max_length')  

        return {
            'input_ids' : input_encodings['input_ids'],
            'attention_mask' : input_encodings['attention_mask'],
            'labels' : target_encodings['input_ids']
        }
    
    
    def convert(self):
        data_samsum = load_from_disk(self.config.data_path)
        data_samsum_pt = data_samsum.map(self.convert_data_to_features, batched = True)
        data_samsum_pt.save_to_disk(os.path.join(self.config.root_dir,"samsum_dataset"))


