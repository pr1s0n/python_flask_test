from sqlalchemy import (
	MetaData, Table, Column, ForeignKey, Interger, String, Date
)

meta = MetaData()
question = Table(
	'question', meta,
	Column('id',Interger,primary_key=True),
	Column('question_text',String(200),nullable=False),
	Column('pub_date',Date,nullable=False)

)
choice = Table(

	'choice',meta,
	Column('id',Interger,primary_key=True),
	Column('choice_text',String(200),nullable=False),
	Column('votes',Interger,server_default='0',nullable=False),
	Column('question',Interger,
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

