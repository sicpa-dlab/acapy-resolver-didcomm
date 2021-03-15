FROM bcgovimages/aries-cloudagent:py36-1.15-0_0.6.0rc0

USER root
COPY ../didcomm_uniresolver aries-acapy-plugin-didcomm-uniresolver/didcomm_uniresolver
COPY ./requirements.txt aries-acapy-plugin-didcomm-uniresolver
COPY ./README.md aries-acapy-plugin-didcomm-uniresolver
COPY ./setup.py aries-acapy-plugin-didcomm-uniresolver
COPY ./docker/default.yml .
RUN chown -R indy:indy aries-acapy-plugin-didcomm-uniresolver
USER $user

# Make ACA-Py Install location more accessible
RUN ln -s /home/indy/.pyenv/versions/3.6.9/lib/python3.6/site-packages site-packages

RUN pip3 install -e ./aries-acapy-plugin-didcomm-uniresolver

ENTRYPOINT ["/bin/bash", "-c", "aca-py \"$@\"", "--"]
CMD ["start", "--arg-file", "default.yml"]