# Langton's Ant API

A simple stateless API that simulates a single step of [Langton's Ant](https://en.wikipedia.org/wiki/Langton%27s_ant) based on the current position, direction, and cell color. Perfect as a starter project to learn APIs, logic flow, and state machines.

---

## Features

- Stateless: no persistent memory between requests
- Implements Langton's Ant rules:
  - On a white square (0): turn right, flip color to 1, move forward
  - On a black square (1): turn left, flip color to 0, move forward
- Returns updated coordinates, direction, and new color

---

## Technologies

- Python
- Flask

---

## Project Structure

```
langtons-ant-api/
├── app.py              # API entry point
├── ant_logic.py        # Core logic for Langton’s Ant
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yourname/langtons-ant-api.git
cd langtons-ant-api
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the API

```bash
python app.py
```

API runs at: `http://127.0.0.1:5000`

---

## API Usage

### POST `/step`

#### Input:
```json
{
  "x": 5,
  "y": 3,
  "dir": "N",
  "cell_color": 0
}
```

- `x`/`y`: Current coordinates
- `dir`: One of `"N"`, `"E"`, `"S"`, `"W"`
- `cell_color`: 0 (white) or 1 (black)

#### Output:
```json
{
  "x": 6,
  "y": 3,
  "dir": "E",
  "new_color": 1
}
```

---

## Example CURL Request

```bash
curl -X POST http://127.0.0.1:5000/step \
  -H "Content-Type: application/json" \
  -d '{"x":5,"y":3,"dir":"N","cell_color":0}'
```

---

## License

MIT
