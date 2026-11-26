// Isolated receipt evidence verifier. Trust key is supplied by the caller;
// never accept a key embedded in the receipt. No network or queue access.
import { verify, createPublicKey } from "node:crypto";
export function verifySignedEvidence({ evidence, signature, publicKey, expected }) {
  try {
    if (!evidence || !expected || typeof signature !== "string" ||
        !/^[A-Za-z0-9_-]{86}$/.test(signature)) return false;
    const fields = ["runId", "workerId", "requestId", "outputSha256"];
    if (!fields.every(k => typeof evidence[k] === "string" && evidence[k].length > 0 &&
        evidence[k] === expected[k])) return false;
    if (!/^[a-f0-9]{64}$/.test(evidence.outputSha256)) return false;
    const key = publicKey?.type === "public" ? publicKey : createPublicKey(publicKey);
    if (key.asymmetricKeyType !== "ed25519") return false;
    const bytes = Buffer.from(signature, "base64url");
    if (bytes.toString("base64url") !== signature) return false;
    return verify(null, Buffer.from(JSON.stringify(["vinterro-receipt-v1",
      ...fields.map(k => evidence[k])])), key, bytes);
  } catch { return false; }
}
