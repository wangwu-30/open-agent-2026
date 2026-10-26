# Zetaris live on Mac mini

- When: 2026-10-26 北京时间 ≈01:00
- Path: `~/zetaris/zetaris-platform`
- verify: 9/9 PASS
- UI: http://localhost:3000
- Evidence: SELECT 1; TPCDS_DB.reason LIMIT 5; NY_TAXI.taxi_zones LIMIT 5
- Secrets: `~/zetaris/registry.env` only
