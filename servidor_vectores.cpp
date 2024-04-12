#include <thrift/concurrency/ThreadManager.h>
#include <thrift/concurrency/ThreadFactory.h>
#include <thrift/protocol/TBinaryProtocol.h>
#include <thrift/server/TSimpleServer.h>
#include <thrift/server/TThreadPoolServer.h>
#include <thrift/server/TThreadedServer.h>
#include <thrift/transport/TServerSocket.h>
#include <thrift/transport/TSocket.h>
#include <thrift/transport/TTransportUtils.h>
#include <thrift/TToString.h>

#include <iostream>
#include <stdexcept>
#include <sstream>
#include <math.h>

#include "CalculadoraVectores.h"

using namespace std;
using namespace apache::thrift;
using namespace apache::thrift::concurrency;
using namespace apache::thrift::protocol;
using namespace apache::thrift::transport;
using namespace apache::thrift::server;

double suma(double n1, double n2)
{
    return n1 + n2;
}

double resta(double n1, double n2)
{
    return n1 - n2;
}

class CalcVectoresHandler : public CalculadoraVectoresIf
{
public:
    CalcVectoresHandler() = default;

    void ping() override
    {
        cout << "Me han hecho Ping()" << endl;
    }

    void sumav(EVector &_return, const EVector &v1, const EVector &v2) override
    {
        _return.elementos.resize(v1.elementos.size());
        _return.longitud = v1.longitud;

        for (int i = 0; i < _return.longitud; i++)
        {
            _return.elementos[i] = v1.elementos[i] + v2.elementos[i];
        }

        cout << "Calculando suma en servidor de vectores\n";
    }

    void restav(EVector &_return, const EVector &v1, const EVector &v2) override
    {
        _return.elementos.resize(v1.elementos.size());
        _return.longitud = v1.longitud;

        for (int i = 0; i < v1.longitud; i++)
        {
            _return.elementos[i] = v1.elementos[i] - v2.elementos[i];
        }

        cout << "Calculando resta en servidor de vectores\n";

    }

    virtual double producto_escalar(const EVector &v1, const EVector &v2) override
    {
        double resultado;

        for (int i = 0; i < v1.longitud; i++)
        {
            resultado += (v1.elementos[i] * v2.elementos[i]);
        }
        cout << "Calculando producto escalar de vectores\n";

        return resultado;
    }

    virtual void producto_vectorial(EVector &_return, const EVector &v1, const EVector &v2) override
    {
        _return.elementos.resize(v1.elementos.size());
        _return.longitud = v1.longitud;

        double x, y, z;
        x = v1.elementos[1] * v2.elementos[2] - v1.elementos[2] * v2.elementos[1];
        y = v1.elementos[2] * v2.elementos[0] - v1.elementos[0] * v2.elementos[2];
        z = v1.elementos[0] * v2.elementos[1] - v1.elementos[1] * v2.elementos[0];

        _return.elementos[0] = x;
        _return.elementos[1] = y;
        _return.elementos[2] = z;

        cout << "Producto vectorial en server de vectores\n";
    }

    virtual void vector_unitario(EVector &_return, const EVector &v) override
    {
        _return.elementos.resize(v.elementos.size());
        _return.longitud = v.longitud;

        double modulo = this->modulo(v);

        double x, y, z;

        if (modulo != 0)
        {
            x = v.elementos[0] / modulo;
            y = v.elementos[1] / modulo;
            z = v.elementos[2] / modulo;
        }
        else
        {
            x = 0;
            y = 0;
            z = 0;
        }

        cout << "Vector unitario calculado en server de vectores\n";

        _return.elementos[0] = x;
        _return.elementos[1] = y;
        _return.elementos[2] = z;
    }

    virtual void multiplicacion_escalar(EVector &_return, const EVector &v1, const double num) override
    {
        _return.elementos.resize(v1.elementos.size());
        _return.longitud = v1.longitud;

        double resultado;
        for (int i = 0; i < v1.longitud; i++)
        {
            resultado = v1.elementos[i] * num;
            _return.elementos[i] = resultado;
        }

        cout << "Multiplicación escalar en server de vectores\n";
    }

    virtual double modulo(const EVector &v) override
    {
        double raiz;

        for (int i = 0; i < v.longitud; i++)
        {
            raiz += v.elementos[i] * v.elementos[i];
        }

        raiz = sqrt(raiz);
        cout << "Modulo en server de vectores\n";

        return raiz;
    }
};

class CalcVectoresCloneFactory : virtual public CalculadoraVectoresIfFactory
{
public:
    ~CalcVectoresCloneFactory() override = default;
    CalculadoraVectoresIf *getHandler(const ::apache::thrift::TConnectionInfo &connInfo) override
    {
        std::shared_ptr<TSocket> sock = std::dynamic_pointer_cast<TSocket>(connInfo.transport);
        cout << "Incoming connection\n";
        cout << "\tSocketInfo: " << sock->getSocketInfo() << "\n";
        cout << "\tPeerHost: " << sock->getPeerHost() << "\n";
        cout << "\tPeerAddress: " << sock->getPeerAddress() << "\n";
        cout << "\tPeerPort: " << sock->getPeerPort() << "\n";
        return new CalcVectoresHandler;
    }

    virtual void releaseHandler(CalculadoraVectoresIf *handler) override
    {
        delete handler;
    }
};

int main()
{
    auto handler = std::make_shared<CalcVectoresHandler>();
    auto processor = std::make_shared<CalculadoraVectoresProcessor>(handler);

    TThreadedServer server(
        processor,
        std::make_shared<TServerSocket>(9092),
        std::make_shared<TBufferedTransportFactory>(),
        std::make_shared<TBinaryProtocolFactory>());

    std::cout << "Iniciando el servidor de vectores..." << std::endl;
    server.serve();
    return 0;
}