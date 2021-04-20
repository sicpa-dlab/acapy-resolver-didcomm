FROM bcgovimages/aries-cloudagent:py36-1.16-0_0.6.0

RUN pip3 install poetry
RUN poetry config virtualenvs.create false

# Make site packages location more accessible (for use with volumes)
RUN ln -s $(pyenv prefix)/lib/python3.6/site-packages site-packages

USER root
RUN mkdir universal-resolver-didcomm
COPY ./README.md universal-resolver-didcomm
COPY ./int/unires/pyproject.toml universal-resolver-didcomm
COPY ./int/unires/default.yml universal-resolver-didcomm
RUN chown -R indy:indy universal-resolver-didcomm
USER $user

WORKDIR universal-resolver-didcomm
RUN poetry install --no-dev

