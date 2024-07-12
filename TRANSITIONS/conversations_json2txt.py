#!/home/jack/miniconda3/envs/cloned_base/bin/python
import json
import os
import shutil

# Define the current directory and the filename for the JSON data
DIR = os.path.dirname(os.path.abspath(__file__))
json_filename = os.path.join(DIR, 'CHATGPT/conversations.json')
print("JSON Filename:", json_filename)

# Read the JSON data from the file
with open(json_filename, 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# Initialize the result string
result_str = ""

# Define a function to get conversation messages similar to the JavaScript logic
def get_conversation_messages(conversation):
    messages = []
    current_node = conversation.get('current_node')
    while current_node:
        node = conversation['mapping'][current_node]
        message = node.get('message')
        if (message and message.get('content') and message['content'].get('content_type') == 'text' and
                len(message['content'].get('parts', [])) > 0 and len(message['content']['parts'][0]) > 0 and
                (message['author']['role'] != 'system' or message.get('metadata', {}).get('is_user_system_message'))):
            author = message['author']['role']
            if author == 'assistant':
                author = 'ChatGPT'
            elif author == 'system' and message['metadata'].get('is_user_system_message'):
                author = 'Custom user info'
            messages.append({'author': author, 'text': message['content']['parts'][0]})
        current_node = node.get('parent')
    return messages[::-1]  # Reverse the list to maintain chronological order

# Iterate over each conversation in the JSON data and process it
for conversation in json_data:
    # Get the conversation title and messages
    title = conversation.get('title', '')
    messages = get_conversation_messages(conversation)

    # Append the title and messages to the result string
    result_str += title + '\n'
    for message in messages:
        result_str += message['author'] + '\n' + message['text'] + '\n'
    result_str += '\n'  # Add a newline between conversations

# Write the processed result string to a text file
txt_filename = json_filename[:-5] + ".txt"  # Change this line to properly handle the filename
print("TXT Filename:", txt_filename)
with open(txt_filename, "w", encoding='utf-8') as output_file:
    result_str = result_str.replace("/n", "\n")
    output_file.write(result_str)

# Copy the generated text file to the parent directory
destination_path = os.path.join(DIR, '..', os.path.basename(txt_filename))
shutil.copy(txt_filename, destination_path)
print("Copied TXT file to:", destination_path)

print("Processing complete. Output written to:", txt_filename)
