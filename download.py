# In this file, we define download_model
# It runs during container build time to get model weights built into the container

# In this example: A Huggingface BERT model

from transformers import T5Tokenizer, T5ForConditionalGeneration
import consts

def download_model():
    tokenizer = T5Tokenizer.from_pretrained(consts.model_name)
    model = T5ForConditionalGeneration.from_pretrained(consts.model_name)

if __name__ == "__main__":
    download_model()
