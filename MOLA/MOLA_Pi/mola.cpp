#include <iostream>
#include <boost/asio.hpp>
#include <boost/array.hpp>
#include <cstring>

using boost::asio::ip::udp;

const int UDP_TX_PACKET_MAX_SIZE = 24; // Adjust size as needed
const unsigned int localPort = 8888; // Local port to listen on

// Buffer to hold incoming packet
char packetBuffer[UDP_TX_PACKET_MAX_SIZE];

int main() {
    try {
        boost::asio::io_service io_service;

        // Create a UDP socket
        udp::socket socket(io_service, udp::endpoint(udp::v4(), localPort));

        while (true) {
            udp::endpoint remote_endpoint;
            boost::system::error_code error;

            // Receive a packet
            size_t len = socket.receive_from(boost::asio::buffer(packetBuffer), remote_endpoint, 0, error);

            if (error && error != boost::asio::error::message_size) {
                throw boost::system::system_error(error);
            }

            std::cout << "Received packet: " << packetBuffer << std::endl;

            // Process the packet
            // Assuming the packet contains comma-separated values
            char* token = strtok(packetBuffer, ",");
            int values[6];
            int index = 0;
            while (token != NULL && index < 6) {
                values[index] = std::atoi(token);
                token = strtok(NULL, ",");
                index++;
            }

            // Assign each item to its own variable
            int t1_cmd = values[0];
            int t2_cmd = values[1];
            int t3_cmd = values[2];
            int t4_cmd = values[3];
            int tz1_cmd = values[4];
            int tz2_cmd = values[5];

            // Print out the values
            std::cout << "t1_cmd: " << t1_cmd << std::endl;
            std::cout << "t2_cmd: " << t2_cmd << std::endl;
            std::cout << "t3_cmd: " << t3_cmd << std::endl;
            std::cout << "t4_cmd: " << t4_cmd << std::endl;
            std::cout << "tz1_cmd: " << tz1_cmd << std::endl;
            std::cout << "tz2_cmd: " << tz2_cmd << std::endl;

            // Clear the buffer for the next packet
            std::memset(packetBuffer, 0, UDP_TX_PACKET_MAX_SIZE);
        }
    } catch (std::exception& e) {
        std::cerr << "Exception: " << e.what() << std::endl;
    }

    return 0;
}