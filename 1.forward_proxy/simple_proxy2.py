import proxy
import ipaddress

if __name__ == '__main__':
    proxy.main(
        hostname=ipaddress.IPv4Address('0.0.0.0'),
        port=9919,
        plugins=['plugin_modify_chunk.ModifyChunkResponsePlugin'],
        ca_cert_file="ca-cert.pem",
        ca_key_file="ca-key.pem",
        ca_signing_key_file="ca-signing-key.pem"
    )
