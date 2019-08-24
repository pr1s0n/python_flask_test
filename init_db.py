from sqlalchemy import create_engine,MetaData
from aiohttp_polls.settings import config
from aiohttp_polls.db import question,choice

DSN = "postgresql://{user}:{password}@{host}:{port}/{database}"

def create_tables(engine):
	meta = MetaData()
	meta.create_all(bind = engine,tables = [question,choice])

def sample_data(engine):
	conn = engine.connect()
	conn.execute(question.insert(),[
		{'question_text' : 'What\s new?',
		 'pub_date' : '2019-08-24 22:42:49.639+02'
		}
	])
	conn.execute(choice.insert(),[
		{'choice_text': 'Not much', 'votes': 0, 'question_id': 1},
        {'choice_text': 'The sky', 'votes': 0, 'question_id': 1},
        {'choice_text': 'Just hacking again', 'votes': 0, 'question_id': 1},
	])
	conn.close()

if __name__ == '__main__':
	db_url = DSN.format(**config['postgres'])
	engine = create_engine(db_url)
	create_tables(engine)
	sample_data(engine)