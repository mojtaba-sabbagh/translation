import sys
#from fairseq.models.transformer import TransformerModel
import os

root_dir = '/home/nlp/users/sabbagh/fairseq'
model_path = '/checkpoints/kabir/transformer_vaswani_wmt_en_de_big'
bpe_path = 'bpe-codes/kabir-code.en'
data_path = 'data-bin/kabir.en-fa'

""" pretrained = TransformerModel.from_pretrained(
     os.path.join(root_dir, model_path),
     checkpoint_file='checkpoint_last.pt',
     data_name_or_path=os.path.join(root_dir, data_path)
     bpe='subword_nmt',
     is_gpu=False,
     bpe_codes=os.path.join(root_dir, bpe_path)
     ) """

def translator(sentence, model):
    dest = 'test'#pretrained.translate(sentence)
    return dest
