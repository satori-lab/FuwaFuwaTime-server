FROM huggingface/transformers-pytorch-cpu

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV TZ JST-9
ENV TERM xterm

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./


RUN pip install --no-cache-dir -r requirements.txt

EXPOSE $PORT
CMD uvicorn main:app --reload --host 0.0.0.0 --port $PORT
