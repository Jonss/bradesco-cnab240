import unittest
from build_cnab_file import generate


class TestBuildCnab240(unittest.TestCase):

    def test_should_generate_cnab_string(self):
        conf = {
            "banco": "237",
            "nome_banco": "BRADESCO S/A",
            "arquivo_nsa": "000001",
            "arquivo_layout": "089",
            "empresa_inscricao_tipo": "2",
            "empresa_inscricao_numero": "49061711000165",
            "empresa_convenio": "0000000",
            "empresa_conta_corrente_agencia": "1234",
            "empresa_conta_corrente_agencia_dv": "5",
            "empresa_conta_corrente_conta_numero": "6789",
            "empresa_conta_corrente_conta_dv": "0",
            "empresa_conta_corrente_digito_verificador": "",
            "empresa_nome": "STEIN E ASSOCIADOS LTDA",
            "empresa_endereco_logradouro": "ALAMEDA VICENTE PINZON",
            "empresa_endereco_numero": "54",
            "empresa_endereco_complemento": "",
            "empresa_endereco_bairro": "VILA OLIMPIA",
            "empresa_endereco_cidade": "SAO PAULO",
            "empresa_endereco_cep": "04547",
            "empresa_endereco_cep_complemento": "130",
            "empresa_endereco_estado": "SP"
        }

        contas = [
            {
                'banco': '237',
                'agencia': '1234',
                'agencia_dv': '',
                'conta': '12344',
                'conta_dv': '5',
                'favorecido_nome': 'JUPITER STEIN',
                'valor_centavos': 1200,
                'data_pagamento': '22052019',
                'cpf': '75110909075'
            },
            {
                'banco': '237',
                'agencia': '1234',
                'agencia_dv': '',
                'conta': '56789',
                'conta_dv': '0',
                'favorecido_nome': 'JOAO SANTANA',
                'valor_centavos': 1000,
                'data_pagamento': '22052019',
                'cpf': '25984162016'
            }
        ]

        cnab_file = generate(conf=conf, contas=contas)
        assert cnab_file is not None
