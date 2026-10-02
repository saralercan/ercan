/**
 * Drag&Drop platform lead normalizer / dedupe contract.
 * Input: CSV records from data/outreach/platforms/*.csv
 * Output: one logical lead per normalized brand identity.
 *
 * Runtime must enrich each lead before Mail Agent can send.
 */

export function normalizeLeadName(input = "") {
  return String(input)
    .toLocaleLowerCase("tr-TR")
    .normalize("NFKD")
    .replace(/\p{M}/gu, "")
    .replace(/&/g, " and ")
    .replace(/[^\p{L}\p{N}]+/gu, " ")
    .trim()
    .replace(/\s+/g, " ");
}

export function mergeLead(existing, incoming) {
  const out = existing || {
    name: incoming.name,
    source_platforms: [],
    source_urls: [],
    email: null,
    phone: null,
    website: null,
    instagram: null,
    city: null,
    region: null,
    country: null,
    product_category: null,
    products: null,
    brand_story: null,
    relationship_status: "unverified",
    gmail_dedupe_status: "pending",
    bounce_status: "unknown",
    enrichment_status: "needs_enrichment",
    outreach_status: "blocked_until_enriched"
  };

  if (incoming.platform && !out.source_platforms.includes(incoming.platform)) {
    out.source_platforms.push(incoming.platform);
  }
  if (incoming.source_url && !out.source_urls.includes(incoming.source_url)) {
    out.source_urls.push(incoming.source_url);
  }
  return out;
}

export function canSendColdOutreach(lead) {
  return Boolean(
    lead &&
    lead.email &&
    lead.product_category &&
    (lead.city || lead.region || lead.country) &&
    lead.brand_story &&
    lead.gmail_dedupe_status === "clear" &&
    lead.bounce_status !== "suppressed" &&
    lead.relationship_status !== "known_historical_hiandco" &&
    lead.relationship_status !== "opted_out" &&
    lead.enrichment_status === "enriched_verified" &&
    lead.outreach_status === "ready_for_personalized_outreach"
  );
}

export const SOURCE_FILES = [
  "data/outreach/platforms/hipicon-2026-10-02.csv",
  "data/outreach/platforms/local-makers-2026-10-02.csv",
  "data/outreach/platforms/hiandco-2026-10-02.csv",
  "data/outreach/platforms/nowshopfun-2026-10-02.csv"
];

export const SOURCE_COUNTS = {
  Hipicon: 2567,
  "Local Makers": 267,
  Hiandco: 197,
  NowShopFun: 271
};

export const SOURCE_ROWS = 3302;
export const UNIQUE_LEADS_AFTER_NAME_DEDUPE = 2895;
export const COLLAPSED_DUPLICATE_ROWS = 407;
