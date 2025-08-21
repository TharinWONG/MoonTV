FROM ghcr.io/moontechlab/lunatv:latest

# Hugging Face 要求使用 7860 port
ENV PORT=7860

EXPOSE 7860

# 假設 lunatv image entrypoint 已經係 node app
CMD ["node", "server.js"]
