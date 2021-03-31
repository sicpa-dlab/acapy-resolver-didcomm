FROM bcgovimages/aries-cloudagent:py36-1.16-0_0.6.0

RUN pip3 install poetry
RUN poetry config virtualenvs.create false

# Make site packages location more accessible (for use with volumes)
RUN ln -s $(pyenv prefix)/lib/python3.6/site-packages site-packages

USER root
COPY ./didcomm_uniresolver aries-acapy-plugin-didcomm-uniresolver/didcomm_uniresolver
COPY ./README.md aries-acapy-plugin-didcomm-uniresolver
COPY ./setup.py aries-acapy-plugin-didcomm-uniresolver
COPY ./pyproject.toml aries-acapy-plugin-didcomm-uniresolver
COPY ./poetry.lock aries-acapy-plugin-didcomm-uniresolver
COPY ./docker/default.yml .
RUN chown -R indy:indy aries-acapy-plugin-didcomm-uniresolver
USER $user

RUN cd aries-acapy-plugin-didcomm-uniresolver; poetry install --no-dev

ENTRYPOINT ["/bin/bash", "-c", "aca-py \"$@\"", "--"]
CMD ["start", "--arg-file", "default.yml"]
