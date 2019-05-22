import argparse
import json
import os
import importlib

import collections
import cnab240.drivers as drivers
import cnab240.core.header_arquivo as ha
import cnab240.core.header_lote as hl
import cnab240.remessa_pagamento as rp


def generate(conf=None, contas=None):
    """Organiza e gera a partir dos parametros enviados o arquivo de remessa.
    """
    odict_ha = ha.default_header_arquivo()
    odict_hl = hl.default_header_lote()
    bla = dict()
    bla['header_arquivo'] = odict_ha
    bla['header_lote'] = odict_hl
    bla['segmento_a_contas'] = contas

    # manda processar
    return rp.generate(bla)
