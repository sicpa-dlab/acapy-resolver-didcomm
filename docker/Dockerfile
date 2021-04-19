FROM bcgovimages/aries-cloudagent:py36-1.16-0_0.6.0

RUN pip3 install poetry
RUN poetry config virtualenvs.create false

# Make site packages location more accessible (for use with volumes)
RUN ln -s $(pyenv prefix)/lib/python3.6/site-packages site-packages

USER root
COPY ./didcomm_resolver aries-acapy-plugin-didcomm-resolver/didcomm_resolver
COPY ./README.md aries-acapy-plugin-didcomm-resolver
COPY ./setup.py aries-acapy-plugin-didcomm-resolver
COPY ./pyproject.toml aries-acapy-plugin-didcomm-resolver
COPY ./poetry.lock aries-acapy-plugin-didcomm-resolver
COPY ./docker/default.yml .
RUN chown -R indy:indy aries-acapy-plugin-didcomm-resolver
USER $user

RUN cd aries-acapy-plugin-didcomm-resolver; poetry install --no-dev
RUN pip3 install -I git+https://github.com/hyperledger/aries-cloudagent-python@main

ENTRYPOINT ["/bin/bash", "-c", "aca-py \"$@\"", "--"]
CMD ["start", "--arg-file", "default.yml"]
