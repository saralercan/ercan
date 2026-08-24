# Go Ayvalık — Firebase App Hosting deployment

Use these exact App Hosting source settings:

- Repository: `saralercan/ercan`
- Branch: `goayvalik-firebase`
- Root directory: `goayvalik`
- Region: `europe-west4`
- Runtime: Node.js 20+
- Framework: Next.js 15.2.9

The live domain `goayvalik.com` must remain on the existing host until the Firebase-generated `*.hosted.app` backend has passed QA.

After backend creation:
1. Create/enable Cloud Firestore in a Europe-compatible location aligned with the product's latency/data requirements.
2. Enable Firebase Authentication providers used by the app (Email/Password and Google).
3. Enable App Check with reCAPTCHA Enterprise, observe telemetry first, then enforce.
4. Apply the repository's Firestore indexes/rules after the first successful build.
5. Seed only verified source-backed content.
6. QA TR/EN, Ayvalık/Cunda/Küçükköy, search, map, routes, events, auth and admin.
7. Use App Hosting's **Migrate a domain** flow for `goayvalik.com`; prepare ownership/TLS before directing traffic.

Never put Firebase Admin credentials or private service-account JSON files in this repository.
