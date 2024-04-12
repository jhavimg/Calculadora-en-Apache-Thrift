/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package calcmatriceshandler;

import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

import org.apache.thrift.TException;
import org.apache.thrift.server.TServer ;
import org.apache.thrift.server.TServer.Args;
import org.apache.thrift.server.TSimpleServer ;
import org.apache.thrift.transport.TSSLTransportFactory;
import org.apache.thrift.transport.TSSLTransportFactory.TSSLTransportParameters;
import org.apache.thrift.transport.TServerSocket ;
import org.apache.thrift.transport.TServerTransport ;

/**
 *
 * @author godoy
 */
public class CalcMatricesHandler implements CalculadoraMatrices.Iface {
    
    public static CalcMatricesHandler handler;
    public static CalculadoraMatrices.Processor processor;
    
    public void ping (){ System.out.println ("Me han hecho ping " );}

    @Override
    public List<List<Double>> sumaM(List<List<Double>> m1, List<List<Double>> m2) throws TException {
        if (m1.size() != m2.size() || m1.get(0).size() != m2.get(0).size()) {
            throw new TException("Las matrices deben tener el mismo tamaño");
        }
        
        List<List<Double>> resultado = new ArrayList<>(m1.size());
        
        for (int i = 0; i < m1.size(); i++) {
            if (m1.get(i).size() != m2.get(i).size()) {
                throw new TException("Las matrices deben tener el mismo tamaño");
            }

            resultado.add(new ArrayList<>(m1.get(i).size()));

            for (int j = 0; j < m1.get(i).size(); j++) {
                resultado.get(i).add(m1.get(i).get(j) + m2.get(i).get(j));
            }
        }
        
        System.out.println("Realizando suma en servidor de matrices");

        return resultado;
    }

    @Override
    public List<List<Double>> restaM(List<List<Double>> m1, List<List<Double>> m2) throws TException {
        if (m1.size() != m2.size() || m1.get(0).size() != m2.get(0).size()) {
            throw new TException("Las matrices deben tener el mismo tamaño");
        }
        
        List<List<Double>> resultado = new ArrayList<>(m1.size());
        
        for (int i = 0; i < m1.size(); i++) {
            if (m1.get(i).size() != m2.get(i).size()) {
                throw new TException("Las matrices deben tener el mismo tamaño");
            }

            resultado.add(new ArrayList<>(m1.get(i).size()));

            for (int j = 0; j < m1.get(i).size(); j++) {
                resultado.get(i).add(m1.get(i).get(j) - m2.get(i).get(j));
            }
        }
        
        System.out.println("Realizando resta en servidor de matrices");

        return resultado;
    }

    @Override
    public List<List<Double>> productoM(List<List<Double>> m1, List<List<Double>> m2) throws TException {
        if (m1.get(0).size() != m2.size()) {
            throw new TException("El número de columnas en la primera matriz debe ser igual al número de filas en la segunda matriz");
        }

        List<List<Double>> resultado = new ArrayList<>(m1.size());
        for (int i = 0; i < m1.size(); i++) {
            resultado.add(new ArrayList<>(Collections.nCopies(m2.get(0).size(), 0.0)));
        }

        for (int i = 0; i < m1.size(); i++) {
            for (int j = 0; j < m2.get(0).size(); j++) {
                for (int k = 0; k < m2.size(); k++) {
                    resultado.get(i).set(j, resultado.get(i).get(j) + (m1.get(i).get(k) * m2.get(k).get(j)));
                }
            }
        }
        
        System.out.println("Realizando producto en servidor de matrices");

        return resultado;
        
    }

    public static void main(String[] args) {
        try {
            handler = new CalcMatricesHandler();
            processor = new CalculadoraMatrices.Processor(handler);
            
            Runnable simple = new Runnable() {
                public void run(){
                    simple (processor);
                }
            };
            
            new Thread(simple).start();
            //new Thread(secure).start();
        } catch (Exception x){
            x.printStackTrace();
        }
        
    }
    
    public static void simple (CalculadoraMatrices.Processor processor){
        try {
            TServerTransport serverTransport = new TServerSocket(9093);
            TServer server = new TSimpleServer(new TServer.Args(serverTransport).processor(processor));
            
            System.out.println("Iniciando servidor de operaciones con matrices...");
            server.serve();
        }catch (Exception e){
            e.printStackTrace();
        }
    }
    
}
