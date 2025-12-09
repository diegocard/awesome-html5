import json
import datetime

# CONFIGURATION
input_file = 'chat_history.json'
output_file = 'chat_history_clean.txt'

def timestamp_to_date(ts):
    if not ts: return "Unknown Date"
    return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')

print(f"Loading {input_file}... (This might take 30 seconds)")

try:
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
except Exception as e:
    print(f"Error loading file: {e}")
    exit()

print(f"Found {len(data)} conversations. Extracting text...")

with open(output_file, 'w', encoding='utf-8') as f:
    # Loop through every conversation
    for convo in data:
        title = convo.get('title', 'Untitled Chat')
        create_time = convo.get('create_time')
        date_str = timestamp_to_date(create_time)

        # Write Header for this chat
        f.write(f"\n\n{'='*50}\n")
        f.write(f"DATE: {date_str} | TITLE: {title}\n")
        f.write(f"{'='*50}\n")

        # Reconstruct the conversation from the 'mapping' tree
        mapping = convo.get('mapping', {})
        current_node = convo.get('current_node')

        # We have to trace backwards from the last message, then reverse it
        messages = []
        while current_node:
            node = mapping.get(current_node)
            if not node: break

            message = node.get('message')
            if message:
                author_role = message.get('author', {}).get('role')
                content = message.get('content', {}).get('parts', [])

                # Extract actual text content
                text_content = ""
                if content and len(content) > 0:
                    text_content = "".join([str(x) for x in content if isinstance(x, str)])

                if text_content and author_role in ['user', 'assistant']:
                    # Format: "User: [text]"
                    messages.append(f"{author_role.upper()}: {text_content}")

            current_node = node.get('parent')

        # Reverse to put in chronological order and write to file
        for msg in reversed(messages):
            f.write(msg + "\n\n")

print(f"SUCCESS! Created {output_file}")
print("You can now open this file in any text editor or upload it to AI tools.")
