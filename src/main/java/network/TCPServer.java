package network;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;

public class TCPServer {
    public static void main(String[] args) throws Exception {
        ServerSocket serverSocket = new ServerSocket(12345); // Choose a suitable port
        System.out.println("Server is running. Waiting for connections...");

        while (true) {
            Socket socket = serverSocket.accept();
            BufferedReader input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            String inputData = input.readLine();
            System.out.println("Received data: " + inputData);
            socket.close();
        }
    }
}
