package network;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.InetAddress;
import java.net.ServerSocket;
import java.net.Socket;
import database.UserDatabase;

public class TCPServer {
    public static void main(String[] args) throws Exception {
        ServerSocket serverSocket = new ServerSocket(12345); // Choose a suitable port
        System.out.println("Server is running. Waiting for connections...");
        try {
            InetAddress inetAddress = InetAddress.getLocalHost();
            String ipAddress = inetAddress.getHostAddress();
            System.out.println("IP Address: " + ipAddress);
        } catch (Exception e) {
            e.printStackTrace();
        }

        while (true) {
            Socket socket = serverSocket.accept();
            BufferedReader input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            String inputData = input.readLine();

            if(inputData.startsWith("GPS")){
                String[] splits = inputData.split("~");
                String username = splits[1];
                String newGPS = splits[2];
                UserDatabase.updateGPS(username,newGPS);

            } else if (inputData.startsWith("UPDATE")) {
                String[] splits = inputData.split("~");
                String username = splits[1];
                String newPassword = splits[2];
                UserDatabase.updatePassword(username,newPassword);

            }else {
                System.out.println("Received data: " + inputData);
            }
            socket.close();
        }
    }
}
