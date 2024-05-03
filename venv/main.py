import nltk
from nltk.chat.util import Chat, reflections

# Function to process the dataset file and extract question-answer pairs
def process_dataset(file_path):
    pairs = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            # Extract question and answer from consecutive lines
            if i < len(lines) - 1:  # Check if there's at least one more line
                question = lines[i].rstrip('?').rstrip('.').strip()
                answer = lines[i + 1].strip()
                pairs.append((question, answer))
            i += 2  # Move to the next question-answer pair
    return pairs

# Main function to create and interact with the chatbot
def main():
    # Path to the dataset file (update this with your file path)
    dataset_file = 'dialogs.txt'

    # Process the dataset file to extract question-answer pairs
    pairs = process_dataset(dataset_file)

    # Create a chatbot instance using the extracted pairs
    chatbot = Chat(pairs, reflections)

    # Chatting loop
    print("Welcome! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("Chatbot:", response)
        if user_input.lower() == 'quit':
            break

if __name__ == "__main__":
    main()
