# LangDetectTrans

LangDetectTrans v0.1

Script to detect language and translate texts to English using MariantMT models, able to
work on a great set of languages. Models can be reviewed on the Hugging Face webpage:

https://huggingface.co/Helsinki-NLP

For this script to properly work, 'transformers', 'torch' and 'pycld3' modules must be installed:

pip install -q transformers
pip install -q torch
pip install -q textblob

# Translation example:

```
text = 'Hola me llamo Camilo'
print(translate_to_english(text))

>> Out: ["Hey, my name's Camilo."]
```