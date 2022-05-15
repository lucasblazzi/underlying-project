FROM public.ecr.aws/lambda/python:3.9
COPY app/ ${LAMBDA_TASK_ROOT}/app
COPY requirements.txt .
RUN pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"
CMD [ "app.app.lambda_hanlder" ]