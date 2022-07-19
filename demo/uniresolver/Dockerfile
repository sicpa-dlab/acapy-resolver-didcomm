FROM bcgovimages/aries-cloudagent:py36-1.16-0_0.7.4

# Make site packages location more accessible (for use with volumes)
RUN ln -s $(pyenv prefix)/lib/python3.6/site-packages site-packages

COPY ./requirements.txt requirements.txt
RUN pip3 install -I --no-cache -r requirements.txt

COPY ./config.yml config.yml

ENTRYPOINT ["/bin/bash", "-c", "aca-py \"$@\"", "--"]
CMD ["start", "--arg-file", "config.yml"]
