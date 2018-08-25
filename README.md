# chatbot
This is a pytorch seq2seq chatbot using

### Clone the project
```sh
$ git clone https://github.com/mvo-projects/chatbot.git
```

### Setup an appropriate environment
Download and install Anaconda or Miniconda

32-bit :
```sh
$ wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86.sh
$ sh Miniconda3-latest-Linux-x86_64.sh
```
64-bit:
```sh
$ wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
$ sh Miniconda3-latest-Linux-x86_64.sh
```
Create an appropriate environment using the spec-file
```sh
$ conda create --name chatbot --file chatbot/spec-file.txt
```

### Download the corpus / models from this drive
[Here](https://drive.google.com/open?id=1BqaIDIR2vJMMCgrFuKBtPo9Px_QXqw2n)

### Setup the config.ini file
An operating manual will be included soon.
But basically the main idea is that you can configure whatever you want from this file like starting a new training (how many layers, the length), resuming an old one, evaluating your models, change corpus... 

This is an example of some parameters and their possible values :

| parameters       | values                  | comments                                                                                |
| ---------------- |:-----------------------:| ---------------------------------------------------------------------------------------:|
| mode             | `train / eval`          | *You can to either training your model or evaluating it*                                |
| use_cuda         | `yes / no`              | *Do you want to use your gpu ?*                                                         |
| corpuspaths      | `path(s)_to_corpus`     | *One or multiples directories separate by a comma*                                      |
| load_encoderpath | `path_to_encoder_model` | *Relative or absolute path to the encoder_model if you want to eval or resume training* |
| load_decoderpath | `path_to_decoder_model` | *Relative or absolute path to the decoder_model if you want to eval or resume training* |

### Activate the environment
```sh
$ source activate chatbot
```

### Lunch the main program
```sh
$ python main.py
```
