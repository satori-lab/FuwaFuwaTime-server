FROM huggingface/transformers-pytorch-cpu

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV TZ JST-9
ENV TERM xterm

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./


RUN pip install --no-cache-dir -r requirements.txt
RUN curl -OL https://github.com/unitaryai/detoxify/releases/download/v0.1-alpha/toxic_multilingual-bbddc277.ckpt
RUN mv toxic_multilingual-bbddc277.ckpt /root/.cache/torch/hub/checkpoints/

EXPOSE 8000
EXPOSE 80
CMD uvicorn main:app
