FROM node:24-bookworm-slim
WORKDIR /app
COPY --chown=node:node package.json package-lock.json ./
RUN npm ci --ignore-scripts --omit=dev --no-audit --no-fund && npm cache clean --force
COPY --chown=node:node pilot.mjs staging.mjs minute-loop.mjs ./
USER node
ENV NODE_ENV=production OPENAI_AGENTS_DISABLE_TRACING=1
CMD ["node","staging.mjs"]
