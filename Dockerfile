# 1. Start with your chosen slim version
FROM python:3.11-slim

# 2. Set the working directory (creates /app if it doesn't exist)
WORKDIR /app

# 3. Copy ONLY the requirements first (for Layer Caching)
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your source code
COPY . .

# 6. The command to run your tests
CMD ["pytest"]
