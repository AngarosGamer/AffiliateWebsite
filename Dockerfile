FROM ubuntu:latest
LABEL authors="angaros"

ENTRYPOINT ["top", "-b"]