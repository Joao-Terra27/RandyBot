import configparser

# -------------------------- Criando/Lendo arquivo CONFIG.INI -------------------------#
config = configparser.ConfigParser()

try:
    with open('.\config.ini') as configfile:
        config.read('.\config.ini')
    for s in config.sections():
        for i in config[s]:
            config[s][i] = config.get(s, i)

except IOError:
    config['CONEXAO'] = \
    {
        'Discord_Token': 'Insira as Informações',
        'Discord_Server': 'Insira as Informações',
    }

    config.write(open('config.ini', 'w'))
