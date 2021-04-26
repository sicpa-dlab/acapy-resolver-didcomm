"""Run Universal Resolver DIDComm + Resolver Plugin Demo."""

import json
import os
import time
from typing import Tuple
from urllib.parse import urlparse, parse_qs
from base64 import b64decode
from colorama import Fore, Style, init
from collections import namedtuple
from . import Agent


init(autoreset=True)


def info(*args):
    """Print info styled text."""
    print("{}{}".format(Fore.BLUE + Style.BRIGHT, " ".join(args)))


def success(*args):
    """Print success styled text."""
    print("{}{}".format(Fore.GREEN + Style.BRIGHT, " ".join(args)))


def fail(*args):
    """Print failure styled text."""
    print("{}{}".format(Fore.RED + Style.BRIGHT, " ".join(args)))


def cont():
    """Prompt for continuation"""
    print("{}{}".format(Fore.BLUE, "Press Enter to continue..."), end="")
    input()


def env_or_input(var, prompt):
    """Return the value of env var or prompt for input."""
    value = os.environ.get(var)
    if not value:
        value = input(prompt)
    return value


def setup() -> Tuple[Agent, dict]:
    """Do agent setup."""
    requester_url = env_or_input("REQUESTER", "Enter the requester URL: ")
    resolver_invite_url = env_or_input(
        "RESOLVER_INVITE", "Enter the resolver invitation: "
    )
    oob = parse_qs(urlparse(resolver_invite_url).query).get("oob")
    if not oob:
        raise Exception("Could not find oob in invitation url")
    resolver_invite_json = json.loads(b64decode(oob[0]))

    # Small version compatibility fixes
    resolver_invite_json["handshake_protocols"][
        0
    ] = "https://didcomm.org/didexchange/1.0"
    resolver_invite_json["services"] = resolver_invite_json["service"]
    del resolver_invite_json["service"]

    info(f"Using Requester Agent API found at {requester_url}")
    requester = Agent(requester_url)
    info("Connecting to Resolver...")
    conn = requester.receive_invite(resolver_invite_json)
    time.sleep(1)
    success("Connected! (connection_id: {})".format(conn["connection_id"]))
    return requester, conn


Inputs = namedtuple("Input", ("dids", "vcs", "methods"))


def get_inputs() -> Inputs:
    """Load inputs for demo."""
    with open("runner/inputs.json") as inputs_file:
        inputs = json.load(inputs_file)

    return Inputs(inputs["dids"], inputs["vcs"], inputs["methods"])


def resolve(requester: Agent, did: str):
    """Resolve a did."""
    info(f"Resolving: {did}")
    try:
        result = requester.resolve(did)
    except Exception as error:
        fail(f"Failed to resolve {did}: {error}")
    else:
        success("Resolved document:")
        print(json.dumps(result, indent=2))


def jsonld_verify(requester, vc: dict):
    """Verify example VC."""
    info("Verifying JSON-LD credential:")
    print(json.dumps(vc, indent=2))

    try:
        result = requester.post(
            "/jsonld/verify",
            return_json=True,
            fail_with="Failed to verify jsonld",
            json={"doc": vc},
        )
    except Exception as error:
        fail(f"Failed to verify cred: {error}")
    else:
        if result["valid"]:
            success("Verified.")
        else:
            fail("Verification failed: {}".format(result["error"]))


def main():
    """Run the demo."""
    requester, connection = setup()
    inputs = get_inputs()

    info("Registering connection to Resolver as a resolver connection...")
    print(f"Using methods {inputs.methods}")
    requester.register_resolver_connection(
        conn_id=connection["connection_id"], methods=inputs.methods
    )
    success("Connection registered.")

    for did in inputs.dids:
        resolve(requester, did)
        cont()

    for vc in inputs.vcs:
        jsonld_verify(requester, vc)
        cont()


if __name__ == "__main__":
    main()
