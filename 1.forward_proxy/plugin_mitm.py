from typing import Optional

from proxy.http.proxy import HttpProxyBasePlugin
from proxy.http.responses import okResponse


class ManInTheMiddlePlugin(HttpProxyBasePlugin):
    """Modifies upstream server responses."""

    def handle_upstream_chunk(self, _chunk: memoryview) -> Optional[memoryview]:
        # return okResponse(content=b'Hello from man in the middle')
        return _chunk