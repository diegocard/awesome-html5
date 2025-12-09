# ChatGPT Export Cleanup Tool

## The Problem: Metadata Bloat

When you export your ChatGPT conversation history, you often encounter a frustrating situation:

- **PDF Export (70MB)**: Smaller but rigid - just "pictures of text" that are hard for computers to process
- **JSON Export (300MB)**: Massive because it stores extensive metadata for every message:
  - Timestamps
  - Model IDs
  - Message IDs
  - Parent node relationships
  - System metadata

For every "Hello" you typed, ChatGPT stores 20+ lines of structural code!

## The Solution

This tool strips the 300MB JSON down to just the human-readable conversation text, reducing it to approximately **15-20MB** of pure content.

## How to Use

### Step 1: Prepare Your Files

1. Create a new folder for your chat cleanup
2. Export your ChatGPT conversations as JSON (from ChatGPT settings)
3. Place the exported JSON file in the folder and rename it to `chat_history.json`
4. Copy `clean_my_chat.py` into the same folder

Your folder structure should look like:
```
my-chat-cleanup/
├── chat_history.json       (your 300MB export)
└── clean_my_chat.py        (this script)
```

### Step 2: Run the Script

Open a terminal in the folder and run:

```bash
python clean_my_chat.py
```

Or if you're using Python 3 specifically:

```bash
python3 clean_my_chat.py
```

The script will:
1. Load your JSON file (this may take 30-60 seconds for large files)
2. Extract all conversations and their messages
3. Create `chat_history_clean.txt` with just the text content

### Step 3: Explore Your Clean Data

You now have a lightweight text file that you can:

#### Option 1: Ask Questions (Google NotebookLM)
- Upload `chat_history_clean.txt` to [NotebookLM](https://notebooklm.google.com/)
- Ask questions like:
  - "Create a timeline of my work on the Python project"
  - "What books did I mention in 2023?"
  - "Summarize my conversations about machine learning"

#### Option 2: Visual Search (VS Code)
- Open the file in [VS Code](https://code.visualstudio.com/) (free)
- Use `Ctrl+F` (Windows/Linux) or `Cmd+F` (Mac) to find keywords instantly
- Use the minimap on the right to quickly scroll through months of conversations

#### Option 3: Local AI (GPT4All - Private)
- Download [GPT4All](https://gpt4all.io/)
- Use the "LocalDocs" feature
- Point it at your `chat_history_clean.txt`
- Chat with a local AI about your documents without data leaving your computer

## Output Format

The cleaned file will have this structure:

```
==================================================
DATE: 2024-01-15 | TITLE: Python Help
==================================================
USER: How do I read a JSON file in Python?

ASSISTANT: You can read a JSON file in Python using the json module...

USER: Thanks! Can you show me an example?

ASSISTANT: Sure! Here's a complete example...


==================================================
DATE: 2024-01-16 | TITLE: Recipe Ideas
==================================================
USER: Give me some healthy breakfast ideas

ASSISTANT: Here are some nutritious breakfast options...
```

## Technical Details

### What Gets Removed
- Message IDs and parent/child relationships
- Model metadata (model version, temperature settings, etc.)
- Plugin and tool invocation data
- System timestamps (except conversation creation date)
- Conversation state management data
- User account metadata

### What Gets Kept
- Conversation titles
- Creation dates (in readable format)
- All user messages
- All assistant responses
- Original conversation order

### File Size Reduction
Typical reduction: **85-95%** of original file size

Example:
- Original JSON: 300MB
- Cleaned text: 15-20MB
- Reduction: ~94%

## Troubleshooting

### "File not found" error
- Make sure `chat_history.json` is in the same folder as the script
- Check that the filename is exactly `chat_history.json` (case-sensitive on Linux/Mac)

### "Invalid JSON" error
- Your export file may be corrupted
- Try exporting again from ChatGPT settings
- Open the JSON file in a text editor to verify it's valid JSON

### Script runs but output is empty
- Your JSON may be in a different format (older export version)
- Check the `mapping` structure in your JSON file
- The script is optimized for the standard OpenAI export format (as of 2024)

### Out of memory errors
- For extremely large files (>500MB), you may need to process in chunks
- Close other applications to free up RAM
- Consider using a machine with more memory

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## License

This tool is provided as-is for personal use in managing your ChatGPT conversation exports.

## Privacy Note

This script runs entirely on your local machine. No data is uploaded or transmitted anywhere. Your conversation history stays on your computer.
