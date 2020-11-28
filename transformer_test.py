import os
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

os.environ["CUDA_VISIBLE_DEVICES"]=""

tokenizer = AutoTokenizer.from_pretrained("Vamsi/T5_Paraphrase_Paws")
model = AutoModelForSeq2SeqLM.from_pretrained("Vamsi/T5_Paraphrase_Paws").to("cpu")

sentence = "This is something which i cannot understand at all"

text =  "paraphrase: " + sentence

encoding = tokenizer.encode_plus(text,pad_to_max_length=True, return_tensors="pt")
input_ids, attention_masks = encoding["input_ids"].to("cpu"), encoding["attention_mask"].to("cpu")

outputs = model.generate(
    input_ids=input_ids, attention_mask=attention_masks,
    max_length=256,
    do_sample=True,
    top_k=200,
    top_p=3.99,
    early_stopping=True,
    num_return_sequences=20
).to("cpu")

for output in outputs:
    line = tokenizer.decode(output, skip_special_tokens=True,clean_up_tokenization_spaces=True)
    print(line)
