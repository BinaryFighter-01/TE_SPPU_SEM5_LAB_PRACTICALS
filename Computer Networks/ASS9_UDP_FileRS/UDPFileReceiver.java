import java.io.*;
import java.net.*;

public class UDPFileReceiver {
    public static void main(String[] args) throws Exception {
        DatagramSocket socket = new DatagramSocket(9877);
        byte[] receiveData = new byte[1024 * 1024]; // 1MB buffer

        DatagramPacket packet = new DatagramPacket(receiveData, receiveData.length);
        socket.receive(packet);

        FileOutputStream fileOutputStream = new FileOutputStream("received_file");
        fileOutputStream.write(packet.getData(), 0, packet.getLength());
        fileOutputStream.close();

        socket.close();
        System.out.println("File received successfully: received_file");
    }
}