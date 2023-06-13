#####
# Build RapiDAST image
#####

# build and install scanners in advance (more scanners will be added)
FROM registry.access.redhat.com/ubi9/python-39

COPY --chown=default . /app
WORKDIR /app

## Install requirements
RUN python3 -m ensurepip --upgrade
RUN pip3 install -U pip
RUN pip3 install -r requirements.txt

ENTRYPOINT ["sh", "container_entrypoint.sh"]
