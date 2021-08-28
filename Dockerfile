FROM huggingface/transformers-pytorch-cpu

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV TZ JST-9
ENV TERM xterm

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./


RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
EXPOSE 80
CMD uvicorn main:app
