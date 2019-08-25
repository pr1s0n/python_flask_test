import aiopg.sa
from sqlalchemy import (
	MetaData, Table, Column, ForeignKey, Integer, String, Date
)
__all__ = ['question','choice']
meta = MetaData()
question = Table(
	'question', meta,
	Column('id',Integer,primary_key=True),
	Column('question_text',String(200),nullable=False),
	Column('pub_date',Date,nullable=False)

)
choice = Table(

	'choice',meta,
	Column('id',Integer,primary_key=True),
	Column('choice_text',String(200),nullable=False),
	Column('votes',Integer,server_default='0',nullable=False),
	Column('question',Integer,
		ForeignKey(

			'question.id',ondelete='CASCADE'
		)
	)
)

#可以用声明式的方式配置数据表
'''
比如：
class Question(Base):
    __tablename__ = 'question'

    id = Column(Integer, primary_key=True)
    question_text = Column(String(200), nullable=False)
    pub_date = Column(Date, nullable=False)

但是这么做没什么好处，SQLALchemy ORM不支持异步，所以不能使用aiopg.sa之类的操作

修改一下代码还可以实现select查询数据：
from sqlalchemy.sql import select
result = await conn.execute(select([Question]))

但是修改和删除操作就比较复杂。

'''

async def init_pg(app):
	conf = app['config']['postgres']
	engine = await aiopg.sa.create_engine(
		database = conf['database'],
		user = conf['user'],
		password = conf['password'],
		host = conf['host'],
		port = conf['port'],
		minsize = conf['minsize'],
		maxsize = conf['maxsize'],
	)
	app['db'] = engine

async def close_pg(app):
	app['db'].close()
	await app['db'].wait_closed()
