service OperacionesAvanzadas {
  void ping(),
  double seno (1:double num),
  double aseno (1: double num),
  double coseno (1:double num),
  double acoseno (1:double num),
  double tangente (1:double num),
  double atangente (1:double num),
  double grados_a_radianes (1:double num),
  double radianes_a_grados (1:double num),
  double potencia (1:double num, 2:double exponente),
  double raizCuadrada(1:i16 numero)
}