from sqlalchemy import Column, String, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from modelos.base import Base


class VeiculoRegistrado(Base.Base, Base):
    __tablename__ = 'veiculo_registrado'

    cod_veiculo = Column(Integer, primary_key=True)
    placa = Column(String)

    carro = relationship('Carro', uselist=False, back_populates='veiculo')
    caminhao = relationship('Caminhao', uselist=False, back_populates='veiculo')
    donos = relationship('Dono', back_populates='veiculo')