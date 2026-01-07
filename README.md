# AttackerKB API

A Python wrapper around the AttackerKB RESTful API. For more details on the API refer to https://api.attackerkb.com/api-docs/docs

## Requirements

- Python 3.10+
- An API key from https://attackerkb.com/

## Installation

```bash
pip install attackerkb-api
```

Or with uv:

```bash
uv add attackerkb-api
```

## Usage

```python
import json
from attackerkb_api import AttackerKB

# Option 1: Pass API key directly
api = AttackerKB(api_key="YOUR_API_KEY")

# Option 2: Use environment variable (ATTACKERKB_API_KEY)
# export ATTACKERKB_API_KEY=your_api_key
api = AttackerKB()

# Get a single topic by ID
result = api.get_single_topic('6f81bc44-c000-427d-b222-b64c29bda621')
print(json.dumps(result, indent=4))

# Search for a CVE by name
result = api.get_topics(name="CVE-2020-10560")
print(json.dumps(result, indent=4))

# Get assessments for a topic
result = api.get_assessments(topicId='131226a6-a1e9-48a1-a5d0-ac94baf8dfd2', page=0, size=2)
print(json.dumps(result, indent=4))

# Get a single assessment by ID
result = api.get_single_assessment('7c324b6e-0d83-4392-a79f-b61220ebfff3')
print(json.dumps(result, indent=4))

# Get a contributor by ID
result = api.get_single_contributor('7ff62803-e0a8-4121-b324-d4afe9f60d43')
print(json.dumps(result, indent=4))

# Get a contributor by username
result = api.get_single_contributor('KevTheHermit')
print(json.dumps(result, indent=4))
```

## API Methods

### Topics

- `get_topics(**kwargs)` - Search for vulnerability topics
- `get_single_topic(topic_id)` - Get a single topic by UUID

### Assessments

- `get_assessments(**kwargs)` - Search for assessments
- `get_single_assessment(assessment_id)` - Get a single assessment by UUID

### Contributors

- `get_contributors(**kwargs)` - Search for contributors
- `get_single_contributor(contributor_id)` - Get a contributor by UUID or username

## Development

Clone the repository and install dependencies with uv:

```bash
git clone https://github.com/kevthehermit/attackerkb-api.git
cd attackerkb-api
uv sync --dev
```

### Running Tests

```bash
export ATTACKERKB_API_KEY=your_api_key
uv run pytest -v --cov=attackerkb_api
```

### Linting

```bash
uv run ruff check .
uv run ruff format --check .
```

## Tools Using This Library

- [AKB-Explorer](https://github.com/horshark/akb-explorer)

## License

MIT
