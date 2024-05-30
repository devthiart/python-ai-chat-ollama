import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # put your server IP address here:
    client.connect(('YOUR_IP_ADDRESS', 12345))

    connected = True

    
    print("***** CHAT WITH ARTIFICIAL INTELLIGENCE *****")
    print("Send a message or type 'exit' to close")

    while connected:
        operation = input("You: ")

        if operation == "exit":
            connected = False
            break

        print("--- waiting... ---")
        
        client.send(operation.encode('utf-8'))

        result = client.recv(4096).decode('utf-8')
        print(f"Ollama A.I.: {result}")

    client.close()

if __name__ == "__main__":
    main()
