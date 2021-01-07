FROM registry.fedoraproject.org/fedora-minimal:33

COPY *.py /app/

WORKDIR /app

VOLUME /app/data

RUN microdnf update && microdnf install python3 python3-flask -y && \
    microdnf clean all

HEALTHCHECK CMD curl --fail http://0.0.0.0:8084/health || exit 1

CMD ["/bin/python3", "app.py"]