FROM mcr.microsoft.com/playwright:v1.41.0-jammy

RUN apt-get update && apt-get install -y python3-pip

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

RUN playwright install chromium

COPY . .

CMD ["pytest", "--alluredir=allure-results"]

