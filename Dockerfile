ARG RUNTIME_VERSION="3.9"

FROM public.ecr.aws/lambda/python:${RUNTIME_VERSION}

ARG BUILD_DEPS="curl"
RUN yum update \
    && yum install ${BUILD_DEPS}

COPY . .

RUN  pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# AS AN EXAMPLE, HAVE A FILE APP.PY WITH A HANDLER FOR THE LAMBDA
# COPY performance_app/app.py ${LAMBDA_TASK_ROOT}
# CMD [ "app.handler" ]

CMD ["/bin/bash"]