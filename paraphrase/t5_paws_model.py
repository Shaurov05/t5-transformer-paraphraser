import os
import random
from .utils import split_into_sentences
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Import the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("Vamsi/T5_Paraphrase_Paws")
model = AutoModelForSeq2SeqLM.from_pretrained("Vamsi/T5_Paraphrase_Paws").to("cpu")

def paraphrase_text(text):
    paraphrased_sentences = []
    paraphrased_text = ""
    sentences = split_into_sentences(text)
    print(sentences)
    for sentence in sentences:
        lines = []
        sentence = "paraphrase: " + sentence
        encoding = tokenizer.encode_plus(sentence, padding=True, return_tensors="pt")
        input_ids, attention_masks = encoding["input_ids"].to("cpu"), encoding["attention_mask"].to("cpu")
        outputs = model.generate(
            input_ids=input_ids,
            attention_mask=attention_masks,
            max_length=256,
            do_sample=True,
            top_k=150,
            top_p=0.99,
            early_stopping=True,
            num_return_sequences=10).to("cpu")
        for output in outputs:
            line = tokenizer.decode(output, skip_special_tokens=True,clean_up_tokenization_spaces=True)
            lines.append(line)
        # Select a random sentence from outputs
        print(lines)
        idx = random.randint(2, 9)
        paraphrased_sentence = lines[idx]
        paraphrased_sentences.append(paraphrased_sentence)
        print(paraphrased_sentences)
    paraphrased_text = " ".join(paraphrased_sentences)
    return paraphrased_text

