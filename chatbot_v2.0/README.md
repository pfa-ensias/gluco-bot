# Rasa Chatbot 

This README file provides instructions on how to run and interact with our Rasa chatbot.

## Prerequisites

Before running the Rasa chatbot, please ensure that you have the following prerequisites installed:

- Python (version 3.6 or later)
- pip (Python package manager)
- Rasa (installed as a Python package)

## Installation

To install Rasa and its dependencies, follow these steps:

1. Open a terminal or command prompt.

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv myenv
   ```
 
3. Activate the virtual environment:
- For Windows:
  ```
  myenv\Scripts\activate
  ```
- For macOS/Linux:
  ```
  source myenv/bin/activate
  ```

4. Install Rasa using pip:
   ```
   pip install rasa
   ```
  
5. Verify the installation by checking the Rasa version:
  ```
  rasa --version
  ```
  
 
## Training the Model

Before running the chatbot, you need to train the model. To do this, follow these steps:

1. Make sure you are in the project directory.

2. Open a terminal or command prompt.

3. Activate the virtual environment (if using one).

4. Run the training command:
  ```
  rasa train
  ```

This command will read your NLU data and domain configuration and train a machine learning model for your chatbot.

5. After training, the model files will be saved in the `models` directory.

## Running the Chatbot

To communicate with the chatbot, you have two options: using the command-line interface (CLI) or interacting with the chatbot in a platform.

### Using the Command-Line Interface (CLI)

To communicate with the chatbot using the CLI, follow these steps:

1. Make sure you have trained the model (see the previous section).

2. Open a terminal or command prompt.

3. Activate the virtual environment (if using one).

4. Run the shell command:
```rasa shell```

This command will start the chatbot in the terminal, allowing you to interact with it.

5. Type your messages or questions and press Enter to get the chatbot's responses.

### Interacting with the Chatbot in a Platform

To interact and test the chatbot in a platform, follow these steps:

1. Make sure you have trained the model (see the previous section).

2. Open a terminal or command prompt.

3. Activate the virtual environment (if using one).

4. Run the following command:
```rasa run -m models --enable-api --cors "*"```

This command will start the chatbot server.

5. Open your preferred platform (e.g., Postman, curl, web browser) to interact with the chatbot's API.

- For example, you can send a POST request to `http://localhost:5005/webhooks/rest/webhook` with a JSON payload containing your message or question. The chatbot will respond with the appropriate response.

- Note: Replace `localhost` with the IP address or domain name where the chatbot server is running.

## Conclusion

With the instructions provided in this README, you should be able to install Rasa, train the model, and interact with the chatbot either using the command-line interface or in a platform. Feel free to customize the chatbot's behavior by modifying the NLU data and domain configuration files.

For more advanced features and capabilities, refer to the official [Rasa documentation](https://rasa.com/docs). If you encounter any issues or have questions, please consult the Rasa community forum or raise an issue on the Rasa GitHub repository.


  
