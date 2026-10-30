# Automated Carrier Parcel Invoice & Money-Back Audit Arbiter Skill

[![GenPark Official](https://img.shields.io/badge/GenPark-Official%20Skill-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-blue)](https://www.linkedin.com/company/92955550)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-green)](https://modelcontextprotocol.io/)
[![Zero Dependency](https://img.shields.io/badge/Dependencies-Zero%20Stdlib-brightgreen)](https://python.org)

FedEx/UPS 50-point automated parcel invoice auditor (late delivery GSR Money-Back Guarantee claims, residential fee surcharges, and incorrect address correction clawbacks). Built for GenPark (https://www.genpark.ai).

## Official Channels
- **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## MCP Tools Exposed
- `audit_carrier_invoice_for_overcharges`: Scan billed parcel shipments against carrier service commitments to detect late deliveries and erroneous surcharges.
- `compile_carrier_gsr_refund_claim`: Generate automated Guaranteed Service Refund (GSR) dispute claim payload for carrier EDI/API submission.

## Installation & Usage
```bash
python -m genpark_agentic_commerce_automated_carrier_invoice_parcel_audit_skill.server --test
```
