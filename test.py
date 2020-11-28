from t5_paws_model import paraphrase_text

data = "There is a USA. embassy. I have a 4.5 cgpa. There is something i don't know? how are you!!!"

data = paraphrase_text(data)
print(data)