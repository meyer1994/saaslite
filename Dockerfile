FROM amazon/aws-lambda-python:3.9

ADD requirements.txt  .
RUN  pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

ADD saaslite ${LAMBDA_TASK_ROOT}/saaslite
ADD handler.py ${LAMBDA_TASK_ROOT}/

CMD [ "handler.handler" ]
