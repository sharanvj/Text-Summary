from TextSummary.config.configuration import ConfigManager
from transformers import Pipeline
from transformers import AutoTokenizer



class PredictionPipeline:
    def __init__(self):
        self.config = ConfigManager().get_model_eval_config()

    def predict(self,text):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)

        gen_kwargs = {"length_penalty": 0.8, "num_beams": 8, "max_length": 128}

        pipe = Pipeline("Summarization", model = self.config.model_path, tokenizer = tokenizer)

        print("Dialouge:")
        print(text)

        output = pipe(text, **gen_kwargs)[0]["summary_text"]

        print("\nModel Summary:")
        print(output)

        return output
    
    