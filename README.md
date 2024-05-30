# AI Chat with Ollama using Python and LangChain

This project is a chat application that integrates with the Ollama AI using the LangChain framework. The application allows users to interact with an AI-powered chatbot through a simple command-line interface.

## Features

- **AI Chat:** Engage in conversations with the Ollama AI.
- **LangChain Framework:** Utilizes the LangChain framework for streamlined AI interaction.
- **Easy to Use:** Simple command-line interface for chatting with the AI.

## Requirements

- Python 3.x
- `Ollama`
- `langchain`

## Installation

1. Install Ollama

    To use this project, you need to have Ollama installed on your machine.
    Install [Ollama](https://ollama.com/) and run `ollama run llama3` to run and chat with Llama 3

2. Clone the repository:

    ```bash
    git clone https://github.com/devthiart/python-ai-chat-ollama
    ```

3. Navigate to the project directory:

    ```bash
    cd python-ai-chat-ollama
    ```

4. Creating a virtual environment and install the required dependencies (Windows):

    `Creating virtual environment:`
    ```bash
    python -m venv langchain
    ```

    `Activate virtual environment:`
    ```bash
    langchain\Scripts\activate
    ```

    `Install dependences:`
    ```bash
    pip install -r requirements.txt
    ```

5. Configure IP address in `server.py` and `client.py` files.

    server.py (line 32):
    ```bash
    # put your computers IP address here:
    server.bind(('YOUR_IP_HERE', 12345))
    ```

    client.py (line 6):
    ```bash
    # put your computers IP address here:
    client.connect(('YOUR_IP_HERE', 12345))
    ```

## Usage

1. Start the server:

    ```bash
    python server.py
    ```

2. In another terminal, start the client and request a translation:

    ```bash
    python client.py
    ```

3. Start chatting with the AI by following the on-screen prompts.

## Example

### Chat Output

```bash
> You: Hello, how are you?
> --- waiting... ---
> Ollama A.I.: I'm just a computer program, so I don't have feelings, but I'm here to help you!
> You: What's the weather like today?
> --- waiting... ---
> Ollama A.I.: I don't have access to real-time data, but you can check a weather website or app for the latest information.
```
