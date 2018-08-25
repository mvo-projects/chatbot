import configparser

def init_config_model(config_name):
    config = configparser.ConfigParser()
    config.read(config_name)
    attn_model = config['model']['attn_model']
    hidden_size = int(config['model']['hidden_size'])
    n_layers = int(config['model']['n_layers'])
    dropout = float(config['model']['dropout'])
    batch_size = int(config['model']['batch_size'])
    optimizer_name = config['model']['optimizer']
    criterion_name = config['model']['criterion']
    
    return (attn_model, hidden_size, n_layers, dropout, batch_size, optimizer_name, criterion_name)

def init_config_training(config_name):
    config = configparser.ConfigParser()
    config.read(config_name)
    clip = float(config['training']['clip'])
    teacher_forcing_ratio = float(config['training']['teacher_forcing_ratio'])
    learning_rate = float(config['training']['learning_rate'])
    decoder_learning_ratio = float(config['training']['decoder_learning_ratio'])
    epoch = int(config['training']['epoch'])
    n_epochs = int(config['training']['n_epochs'])
    save_every = int(config['training']['save_every'])
    print_every = int(config['training']['print_every'])
    evaluate_every = int(config['training']['evaluate_every'])
    use_cuda = config['training'].getboolean('use_cuda')
    save_encoderpath = config['training']['save_encoderpath']
    save_decoderpath = config['training']['save_decoderpath']
    
    return (clip, teacher_forcing_ratio, learning_rate, decoder_learning_ratio, epoch, n_epochs, save_every, print_every, evaluate_every, use_cuda, save_encoderpath, save_decoderpath)

def init_config_load(config_name):
    config = configparser.ConfigParser()
    config.read(config_name)
    load_training = config['load'].getboolean('load_training')
    load_encoderpath = config['load']['load_encoderpath']
    load_decoderpath = config['load']['load_decoderpath']
    
    return (load_training, load_encoderpath, load_decoderpath)
    

def init_config_eval(config_name):
    config = configparser.ConfigParser()
    config.read(config_name)
    MAX_LENGTH = int(config['eval']['max_length'])
    use_cuda = config['eval'].getboolean('use_cuda')
    learning_rate = float(config['training']['learning_rate'])
    decoder_learning_ratio = float(config['training']['decoder_learning_ratio'])
    temp_module_name = config['eval']['temperature_module_name']
    temp_function_name = config['eval']['temperature_function_name']
    n_words_vocab = int(config['eval']['n_words_vocab'])
    
    return (MAX_LENGTH, use_cuda, learning_rate, decoder_learning_ratio, temp_module_name, temp_function_name, n_words_vocab)

def init_config_data(config_name):
    config = configparser.ConfigParser()
    config.read(config_name)
    corpuspaths = []
    qapairspath = []
    MIN_LENGTH = int(config['data']['min_length'])
    MAX_LENGTH = int(config['data']['max_length'])
    
    USE_QACORPUS = config['data'].getboolean('use_qacorpus')
    CREATE_QAPAIRS = config['data'].getboolean('create_qapairs')
    if (not(USE_QACORPUS)):
        corpuspaths = config['data']['corpuspaths'].split(',')
    else:
        if CREATE_QAPAIRS:
            corpuspaths = config['data']['qacorpuspaths'].split(',')
        else:
            qapairspath = config['data']['qapairspath']
    
    return (MIN_LENGTH, MAX_LENGTH, USE_QACORPUS, CREATE_QAPAIRS, corpuspaths, qapairspath)

def init_config_getmode(config_name):
    config = configparser.ConfigParser()
    config.read(config_name)
    mode = config['init']['mode']
    
    return mode