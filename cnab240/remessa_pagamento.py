import cnab240.core.header_arquivo as ha
import cnab240.core.trailer_arquivo as ta

def generate(odict_entrada):

    
    str_header = ha.header_arquivo( odict_entrada['header_arquivo'] )
    #str_trailer = ta.trailer_arquivo( odict_entrada['trailer_arquivo'])
    _str = str_header+"\n"

    return _str
  