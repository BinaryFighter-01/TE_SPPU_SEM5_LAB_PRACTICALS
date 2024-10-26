import java.io.*;
import java.net.*;

public class UDPFileSender {
    public static void main(String[] args) throws Exception {
        if (args.length != 1) {
            System.out.println("Usage: java UDPFileSender <filename>");
            return;
        }

        File file = new File(args[0]);
        byte[] fileData = new byte[(int) file.length()];
        new FileInputStream(file).read(fileData);

        DatagramSocket socket = new DatagramSocket();
        InetAddress address = InetAddress.getByName("localhost");
        DatagramPacket packet = new DatagramPacket(fileData, fileData.length, address, 9877);
        socket.send(packet);

        socket.close();
        System.out.println("File sent successfully");
    }
}