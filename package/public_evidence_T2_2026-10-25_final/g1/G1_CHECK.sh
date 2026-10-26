#!/usr/bin/env bash
# G1_CHECK.sh <owner_public_key.pub> [<c2_chain_r3k.py>]   - PREPARED, NOT RUN (owner provides the public key separately)
# Checks that the owner-supplied PUBLIC key verifies the frozen mandate signature, using the namespace and principal
# measured from the frozen run material: namespace eve-057-live-go (RUN_TASK_LGX_WSL_r4_T2.sh line 412, client
# c2_chain_r3k.py lines 52 and 85), principal eve-057-owner (client lines 53 and 85).
# Optional 2nd argument: the run client (must be sha256 dc00624391985ae02c2fe62ef4fa0164d5d54d4869e23a57dce7e4990603c525,
# pinned by MANDATE line 5); the key pinned in its OWNER_ALLOWED_SIGNERS line is then compared with the supplied key.
# Reads only the files named here. Never reads ~/.ssh. Refuses any file containing private key material.
# Proves (on exit 0): the signature over these exact mandate bytes was made with the private key matching this public
# key. Does NOT prove who controls that key.
set -u
PUB="${1:?usage: G1_CHECK.sh <owner_public_key.pub> [<c2_chain_r3k.py>]}"; CLIENT="${2:-}"
HERE="$(cd "$(dirname "$0")/.." && pwd)"
M="$HERE/evidence/chain02/r2/missions/LGX-T2-QUOTE/MANDATE_LGX-T2-QUOTE-20261024T130334Z.txt"
S="$M.sig"
MSHA=4494612f489fb858780906075880900e51181a564d2648be277bca68f942eaab
SSHA=633bee9a64969a0bb72fb83b76227884d4aa6265a68dd23287efda9baea13338
CSHA=dc00624391985ae02c2fe62ef4fa0164d5d54d4869e23a57dce7e4990603c525
[ "$(sha256sum "$M" | cut -c1-64)" = "$MSHA" ] || { echo "STOP mandate sha256 differs"; exit 3; }
[ "$(sha256sum "$S" | cut -c1-64)" = "$SSHA" ] || { echo "STOP signature sha256 differs"; exit 3; }
grep -q 'PRIVATE KEY' "$PUB" && { echo "STOP the supplied file contains private key material - nothing done"; exit 3; }
KEY=$(awk 'NF>=2 && $1=="ssh-ed25519" {print $1" "$2; exit}' "$PUB")
[ -n "$KEY" ] || { echo "STOP no ssh-ed25519 public key line in $PUB"; exit 3; }
echo "supplied public key file sha256 $(sha256sum "$PUB" | cut -c1-64)"
if [ -n "$CLIENT" ]; then
  [ "$(sha256sum "$CLIENT" | cut -c1-64)" = "$CSHA" ] || { echo "STOP client sha256 is not the mandate-pinned client"; exit 3; }
  PIN=$(grep -E "^OWNER_ALLOWED_SIGNERS = " "$CLIENT" | grep -oE "ssh-ed25519 [A-Za-z0-9+/=]+")
  [ "$PIN" = "$KEY" ] && echo "PIN_MATCH supplied key == key pinned in the mandate-pinned client" || { echo "PIN_DIFFERS supplied key != pinned key"; exit 4; }
fi
T=$(mktemp -d); printf 'eve-057-owner namespaces="eve-057-live-go" %s\n' "$KEY" > "$T/allowed_signers"
ssh-keygen -Y verify -f "$T/allowed_signers" -I eve-057-owner -n eve-057-live-go -s "$S" < "$M"; rc=$?
rm -r "$T"
[ $rc -eq 0 ] && echo "RESULT G1_SIGNATURE_VERIFIES (key control / identity NOT established by this check)" || echo "RESULT G1_FAIL rc=$rc"
exit $rc
