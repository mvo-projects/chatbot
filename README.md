# chatbot
This is a PyTorch seq2seq chatbot based on [the official PyTorch tutorial](https://pytorch.org/tutorials/intermediate/seq2seq_translation_tutorial.html) using OpenSubtitles corpus.

### Clone the project
```sh
$ git clone https://github.com/mvo-projects/chatbot.git
```

### Setup an appropriate environment
Download and install Anaconda or Miniconda

#### Linux
32-bit :
```sh
$ wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86.sh
$ sh Miniconda3-latest-Linux-x86.sh
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

#### Mac OS

64-bit :
```sh
$ curl -0 https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
$ sh Miniconda3-latest-MacOSX-x86_64.sh
```
Create an appropriate environment using the spec-file
```sh
$ conda create --name chatbot --file chatbot/spec-file-osx.txt
```

### Download the corpus / models from this drive
[Here](https://drive.google.com/open?id=1BqaIDIR2vJMMCgrFuKBtPo9Px_QXqw2n)

### Setup the config.ini file
An operating manual will be included soon.
But basically the main idea is that you can configure whatever you want from this file like starting a new training (how many layers, the length), resuming an old one, evaluating your models, change corpus... 

This is an example of some parameters and their possible values :

| parameters       | values                  | comments                                                                                |
| ---------------- |:-----------------------:| ---------------------------------------------------------------------------------------:|
| mode             | `train / eval`          | *You can either train your model or evaluate it*                                        |
| use_cuda         | `yes / no`              | *Do you want to use your gpu ?*                                                         |
| corpuspaths      | `path(s)_to_corpus`     | *One or multiples directories separate by a comma*                                      |
| load_encoderpath | `path_to_encoder_model` | *Relative or absolute path to the encoder_model if you want to eval or resume training* |
| load_decoderpath | `path_to_decoder_model` | *Relative or absolute path to the decoder_model if you want to eval or resume training* |

### Activate the environment
```sh
$ source activate chatbot
```

### Launch the main program using the appropriate config_file for your model
```sh
$ python main.py [config_file.ini]
```
