from sqlalchemy import create_engine
from app.base.vendorcodebase import Base_vс
from app.base.stockbase import Base_st
from app.base.inputposbase import Base_ip
from app.base.inputwaybillbase import Base_iw
from app.base.outputposbase import Base_op
from app.base.outputwaybillbase import Base_ow


def create_database():
    engine = new_connect()
    Base_vс.metadata.create_all(engine)
    Base_iw.metadata.create_all(engine)
    Base_ip.metadata.create_all(engine)
    Base_st.metadata.create_all(engine)
    Base_ow.metadata.create_all(engine)
    Base_op.metadata.create_all(engine)


def new_connect():
    engine = create_engine("postgresql+psycopg2://admin:admin@192.168.56.106:5432/stock", echo=True)
    engine.connect()
    return engine


if __name__ == '__main__':
    create_database()
