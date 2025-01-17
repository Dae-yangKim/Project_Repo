# 파이썬 3.9 slim으로 설정
FROM python:3.9-slim
# 현재 디렉토리 파일을 app에 복사
COPY . /app
# /backend 디렉토리 설정
WORKDIR /app
# 의존성 파일 복사
COPY requirements.txt .
# 의존성 설치 커맨드 실행
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir flask 
    # Flask 설치
# 컨테이너에 Flask 코드 복사
COPY . .
# 5000 포트 설정
EXPOSE 5000
# python app.py를 실행한다
CMD ["python" , "./app.py"]