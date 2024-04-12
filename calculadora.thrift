struct EVector {
  1: list<double> elementos,
  2: i16 longitud,
}

service Calculadora{
    void ping(),
    double suma (1:double num1, 2:double num2),
    double resta (1:double num1, 2:double num2),
    double multiplicacion (1:double num1, 2:double num2),
    double division (1:i16 num1, 2:i16 num2),

    double seno (1:double num),
    double aseno (1:double num),
    double coseno (1:double num),
    double acoseno (1:double num),
    double tangente (1:double num),
    double atangente (1:double num),
    double grados_a_radianes (1:double num),
    double radianes_a_grados (1:double num),
    double potencia (1:double num, 2:double exponente),
    double raizCuadrada(1:double numero), 

    EVector sumav(1:EVector v1, 2:EVector v2),
    EVector restav(1:EVector v1, 2:EVector v2),
    double producto_escalar(1:EVector v1, 2:EVector v2),
    EVector producto_vectorial(1:EVector v1, 2:EVector v2),
    EVector vector_unitario(1:EVector v),
    EVector multiplicacion_escalar(1:EVector v1, 2:double num),
    double modulo(1:EVector v),

    list<list<double>> sumaM(1:list<list<double>> m1, 2:list<list<double>> m2),
    list<list<double>> restaM(1:list<list<double>> m1, 2:list<list<double>> m2),
    list<list<double>> productoM(1:list<list<double>> m1, 2:list<list<double>> m2),
}