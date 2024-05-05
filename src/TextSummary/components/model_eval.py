from transformers import T5Tokenizer, T5ForConditionalGeneration
from datasets import load_dataset, load_from_disk, load_metric
from TextSummary.entity import ModelEvalConfig
import torch
from tqdm import tqdm
import pandas as pd

class ModelEval:
    def __init__(self,config: ModelEvalConfig):
        self.config = config

    def generate_batch_sized_chunks(self, list_of_elements, batch_size):
        for i in range(0, len(list_of_elements), batch_size):
            yield list_of_elements[i:i+batch_size]

    def calculate_metric(self, dataset, metric, model, tokenizer, batch_size = 16, device = "mps" if torch.backends.mps.is_available() else "cpu", column_text = "dialogue", column_summary= "summary"):
        test_data_batches = list(self.generate_batch_sized_chunks(dataset[column_text], batch_size))

        target_test_data_batches = list(self.generate_batch_sized_chunks(dataset[column_summary], batch_size))

        for test_data, target_test_data in tqdm(zip(test_data_batches,target_test_data_batches), total= len(test_data_batches)):

            inputs = tokenizer(test_data, max_length = 1024, truncation = True, padding = "max_length", return_tensors = "pt")

            summaries = model.generate(input_ids = inputs["input_ids"].to(device), attention_mask = inputs["attention_mask"].to(device), length_penalty = 0.8, num_beams = 8, max_length=128)

            decoded_summaries = [tokenizer.decode(s,skip_special_tokens=True, clean_up_tokenization_spaces = True) for s in summaries]

            decoded_summaries = [f.replace(""," ") for f in decoded_summaries]

            metric.add_batch(predictions = decoded_summaries, references = target_test_data)

        score = metric.compute()
        return score



    def evaluate(self):
        device = "mps" if torch.backends.mps.is_available() else "cpu"
        tokenizer = T5Tokenizer.from_pretrained(self.config.tokenizer_path)
        model_t5 = T5ForConditionalGeneration.from_pretrained(self.config.model_path).to(device)

        dataset = load_from_disk(self.config.data_path)

        rouge_names = ["rouge1","rouge2","rougeL","rougeLsum"]

        rouge_metric = load_metric('rouge')

        score = self.calculate_metric(dataset['test'], rouge_metric, model_t5, tokenizer, batch_size = 2,column_text='dialogue', column_summary= 'summary')

        rouge_dict = dict((rn, score[rn].mid.fmeasure) for rn in rouge_names)
        df = pd.DataFrame(rouge_dict, index= ['T5-Small'])
        df.to_csv(self.config.metric_file_name, index=False)


