# MongoDB ObjectId Decoder

This is a simple Python script to decode MongoDB ObjectIds into their 
constituent parts: timestamp, machine identifier, process identifier, 
and counter.

## Requirements

- Python 3.x
- pymongo

## Installation

1. Clone the repository or download the script.

2. Navigate to the project directory:

```bash
cd mongo-id-decoder
```

3. Create a virtual environment and activate (recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

4. Install the required Python packages

```bash
pip install -r requirements.txt
```

5. Ready to go! Provide an object id as the first argument or enter it 
at the prompt.

```bash
python3 mongo-id-decoder.py 507f1f77bcf86cd799439011
```

6. Make it executable (optional)

```bash
chmod +x mongo-id-decoder.py
```