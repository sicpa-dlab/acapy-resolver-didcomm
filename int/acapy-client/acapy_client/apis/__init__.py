
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.action_menu_api import ActionMenuApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from acapy_client.api.action_menu_api import ActionMenuApi
from acapy_client.api.basicmessage_api import BasicmessageApi
from acapy_client.api.connection_api import ConnectionApi
from acapy_client.api.credential_definition_api import CredentialDefinitionApi
from acapy_client.api.credentials_api import CredentialsApi
from acapy_client.api.did_exchange_api import DidExchangeApi
from acapy_client.api.didcomm_resolver_api import DidcommResolverApi
from acapy_client.api.endorse_transaction_api import EndorseTransactionApi
from acapy_client.api.introduction_api import IntroductionApi
from acapy_client.api.issue_credential_v1_0_api import IssueCredentialV10Api
from acapy_client.api.issue_credential_v2_0_api import IssueCredentialV20Api
from acapy_client.api.jsonld_api import JsonldApi
from acapy_client.api.ledger_api import LedgerApi
from acapy_client.api.mediation_api import MediationApi
from acapy_client.api.out_of_band_api import OutOfBandApi
from acapy_client.api.present_proof_v1_0_api import PresentProofV10Api
from acapy_client.api.present_proof_v2_0_api import PresentProofV20Api
from acapy_client.api.resolver_api import ResolverApi
from acapy_client.api.revocation_api import RevocationApi
from acapy_client.api.schema_api import SchemaApi
from acapy_client.api.server_api import ServerApi
from acapy_client.api.trustping_api import TrustpingApi
from acapy_client.api.wallet_api import WalletApi
