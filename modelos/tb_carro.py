from sqlalchemy import Column, String, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from modelos.base import Base


class Carro(Base.Base, Base):
    __tablename__ = 'carro'

    cod_veiculo = Column(Integer, ForeignKey('veiculo_registrado.cod_veiculo'), primary_key=True)
    estilo = Column(String)
    marca_carro = Column(String)
    modelo_carro = Column(String)
    ano_carro = Column(Integer)

    veiculo = relationship('VeiculoRegistrado', back_populates='carro')