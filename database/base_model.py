from sqlalchemy.ext.declarative import declarative_base


class PreBase:
    """Класс, от которого будут наследоваться все модели"""
    
    pass

Base = declarative_base(cls=PreBase)