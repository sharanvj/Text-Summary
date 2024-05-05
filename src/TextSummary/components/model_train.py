from transformers import TrainingArguments, Trainer, EarlyStoppingCallback
from transformers import DataCollatorForSeq2Seq
from transformers import T5Tokenizer, T5ForConditionalGeneration
from datasets import load_dataset, load_from_disk
from TextSummary.entity import ModelTrainingConfig
import torch
import os


class ModelTrainer:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config


    
    def train(self):
        #device = "cuda" if torch.cuda.is_available() else "cpu"
        os.environ['PYTORCH_MPS_HIGH_WATERMARK_RATIO'] = '0.0'
        device = "mps" if torch.backends.mps.is_available() else "cpu"
        tokenizer = T5Tokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = T5ForConditionalGeneration.from_pretrained(self.config.model_ckpt).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)
        
        #loading data 
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        # trainer_args = TrainingArguments(
        #     output_dir=self.config.root_dir, num_train_epochs=self.config.num_train_epochs, warmup_steps=self.config.warmup_steps,
        #     per_device_train_batch_size=self.config.per_device_train_batch_size, per_device_eval_batch_size=self.config.per_device_train_batch_size,
        #     weight_decay=self.config.weight_decay, logging_steps=self.config.logging_steps,
        #     evaluation_strategy=self.config.evaluation_strategy, eval_steps=self.config.eval_steps, save_steps=1e6,
        #     gradient_accumulation_steps=self.config.gradient_accumulation_steps
        # ) 


        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir, num_train_epochs=5, warmup_steps=500,
            per_device_train_batch_size=1, per_device_eval_batch_size=1,
            weight_decay=0.01, logging_steps=10,
            evaluation_strategy='steps', eval_steps=500, save_steps=1e6,
            gradient_accumulation_steps=16, load_best_model_at_end=True
        )

        early_stopping_callback = EarlyStoppingCallback(
            early_stopping_patience=3,
            early_stopping_threshold=0.00)

        trainer = Trainer(model=model_pegasus, args=trainer_args,
                  tokenizer=tokenizer, data_collator=seq2seq_data_collator,
                  train_dataset=dataset_samsum_pt["train"], 
                  eval_dataset=dataset_samsum_pt["validation"],
                  callbacks=[early_stopping_callback])
        
        trainer.train()

        
        model_pegasus.save_pretrained(os.path.join(self.config.root_dir,"T5-samsum-model"))
        
        tokenizer.save_pretrained(os.path.join(self.config.root_dir,"tokenizer"))