import logging
import pprint
from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Interpreter
from rasa_nlu.evaluate import run_evaluation


logfile = 'nlu_model.log'


def train_nlu(data_path, configs, model_path):
    logging.basicConfig(filename=logfile, level=logging.DEBUG)
    training_data = load_data(data_path)
    trainer = Trainer(config.load(configs))
    trainer.train(training_data)
    model_directory = trainer.persist(model_path, project_name='current', fixed_model_name='nlu')
    run_evaluation(data_path, model_directory)


def run_nlu(nlu_path):
    logging.basicConfig(filename=logfile, level=logging.DEBUG)
    interpreter = Interpreter.load(nlu_path)
    pprint.pprint(interpreter.parse("Share some latest news around the world?"))
    pprint.pprint(interpreter.parse("What is going on in technology?"))
    pprint.pprint(interpreter.parse("What is going on in education?"))
    pprint.pprint(interpreter.parse("Thank you"))
    pprint.pprint(interpreter.parse("Thank you so much"))
    pprint.pprint(interpreter.parse("Thanks"))
    pprint.pprint(interpreter.parse("Help me find some movie reviews about avatar"))
    pprint.pprint(interpreter.parse("Help me find some movie reviews about godfather"))
    pprint.pprint(interpreter.parse("I want to read some movie reviews about godfather"))
    pprint.pprint(interpreter.parse("Could you show me the articles about automobiles?"))
    pprint.pprint(interpreter.parse("Could you show me the articles about home?"))
    pprint.pprint(interpreter.parse("Could you show me the articles about politics?"))
    pprint.pprint(interpreter.parse("Show me the most viewed articles about travel"))
    pprint.pprint(interpreter.parse("Show me the most viewed articles about theater"))    


if __name__ == '__main__':
    train_nlu('./nlu/nlu_data.md', './nlu/nlu_config.yml', './models')
    run_nlu('./models/current/nlu')
