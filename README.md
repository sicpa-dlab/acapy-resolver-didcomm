ACA-Py Plugin - DIDCOMM Universal Resolver
=======================================

This plugin provides an ACA-Py DID Resolver interface to a Universal
Resolver instance over DIDComm messaging.

## Installation and Usage

First, install this plugin into your environment.

```sh
$ pip install git+https://github.com/rd-dlab/aries-acapy-plugin-did-comm-uniresolver.git
```

When starting up ACA-Py, load the plugin along with any other startup
parameters.

```sh
$ aca-py start --arg-file my_config.yml --plugin did_comm_uniresolver
```
