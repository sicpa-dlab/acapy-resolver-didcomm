import pytest

'''HOSTS = [("resolver", 3201), ("requester", 3203)]
MAX_RETRIES = 5

@pytest.fixture(scope="session", autouse=True)
async def agents_ready():
    """Wait for the agents to be ready."""

    def can_connect(host, port):
        with closing(
            socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ) as sock:
            return sock.connect_ex((host, port)) == 0

    for host in HOSTS:
        attempt = 0
        while not can_connect(*host):
            attempt += 1
            if attempt > MAX_RETRIES:
                raise RuntimeError(
                    'Could not connect to server at {}:{}'.format(host, port)
                )
            await asyncio.sleep(1)'''

def test_pass():
    pass