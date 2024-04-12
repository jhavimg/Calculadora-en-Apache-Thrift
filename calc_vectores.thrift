struct EVector {
  1: list<double> elementos,
  2: i16 longitud,
}

service CalculadoraVectores {
  void ping(),
  EVector sumav(1:EVector v1, 2:EVector v2),
  EVector restav(1:EVector v1, 2:EVector v2),
  double producto_escalar(1:EVector v1, 2:EVector v2),
  EVector producto_vectorial(1:EVector v1, 2:EVector v2),
  EVector vector_unitario(1:EVector v),
  EVector multiplicacion_escalar(1:EVector v1, 2:double num),
  double modulo(1:EVector v),
}