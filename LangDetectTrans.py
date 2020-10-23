from textblob import TextBlob
from transformers import MarianTokenizer, MarianMTModel


def get_lang_group(source_lang):

  gp = source_lang
  
  GROUP_MEMBERS = {
  'ZH': ['cmn', 'cn', 'yue', 'ze_zh', 'zh_cn', 'zh_CN', 'zh_HK', 'zh_tw', 'zh_TW', 'zh_yue', 'zhs', 'zht', 'zh'],
  'ROMANCE': ['fr', 'fr_BE', 'fr_CA', 'fr_FR', 'wa', 'frp', 'oc', 'ca', 'rm', 'lld', 'fur', 'lij', 'lmo', 'es', 'es_AR', 'es_CL', 'es_CO', 'es_CR', 'es_DO', 'es_EC', 'es_ES', 'es_GT', 'es_HN', 'es_MX', 'es_NI', 'es_PA', 'es_PE', 'es_PR', 'es_SV', 'es_UY', 'es_VE', 'pt', 'pt_br', 'pt_BR', 'pt_PT', 'gl', 'lad', 'an', 'mwl', 'it', 'it_IT', 'co', 'nap', 'scn', 'vec', 'sc', 'ro', 'la'],
  'NORTH_EU': ['de', 'nl', 'fy', 'af', 'da', 'fo', 'is', 'no', 'nb', 'nn', 'sv'],
  'SCANDINAVIA': ['da', 'fo', 'is', 'no', 'nb', 'nn', 'sv'],
  'SAMI': ['se', 'sma', 'smj', 'smn', 'sms'],
  'NORWAY': ['nb_NO', 'nb', 'nn_NO', 'nn', 'nog', 'no_nb', 'no'],
  'CELTIC': ['ga', 'cy', 'br', 'gd', 'kw', 'gv']
  }
  
  for group, lang_list in GROUP_MEMBERS.items():
    for lang in lang_list:
      if lang == source_lang:
        gp = group
        break

  return gp

def translate_to_english(text,source_lang): #Translation function
    
  model_name = f'Helsinki-NLP/opus-mt-{get_lang_group(source_lang)}-{"en"}'
 
  model = MarianMTModel.from_pretrained(model_name)               #Loads the MarianMT model
  tokenizer = MarianTokenizer.from_pretrained(model_name)
  batch = tokenizer.prepare_seq2seq_batch(src_texts=[text])  #Creates word batches for the sequential passing to the model
  generate_model = model.generate(**batch)  
  #translation: List[str] = tokenizer.batch_decode(generate_model, skip_special_tokens=True)  #Translation
  translation = tokenizer.batch_decode(generate_model, skip_special_tokens=True)
  
  return translation
