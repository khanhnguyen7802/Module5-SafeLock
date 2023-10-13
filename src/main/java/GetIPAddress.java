import java.net.InetAddress;

public class GetIPAddress {
    public static void main(String[] args) {
        try {
            InetAddress inetAddress = InetAddress.getLocalHost();
            String ipAddress = inetAddress.getHostAddress();
            System.out.println("IP Address: " + ipAddress);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
