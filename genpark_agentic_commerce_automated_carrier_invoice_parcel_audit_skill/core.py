# -*- coding: utf-8 -*-
"""Automated Carrier Parcel Invoice Audit Arbiter for GenPark Agentic Commerce."""
import json
from typing import Dict, Any, List

class CarrierInvoiceParcelAuditArbiter:
    @staticmethod
    def audit_carrier_invoice_for_overcharges(billed_shipments: List[Dict[str, Any]]) -> Dict[str, Any]:
        disputed_items = []
        total_recovery = 0.0
        
        for item in billed_shipments:
            tracking = item.get("tracking_number", "TRK-000")
            delivered_epoch = item.get("actual_delivery_epoch", 0)
            committed_epoch = item.get("committed_delivery_epoch", 0)
            rate = float(item.get("billed_amount_usd", 0.0))
            
            # Late delivery check (GSR)
            if delivered_epoch > committed_epoch and not item.get("weather_delay_flag", False):
                disputed_items.append({
                    "tracking": tracking,
                    "reason": "LATE_DELIVERY_GUARANTEED_SERVICE_REFUND",
                    "refund_eligible_usd": rate
                })
                total_recovery += rate
            elif item.get("address_correction_fee_usd", 0.0) > 0 and item.get("address_verified_pre_ship", False):
                fee = float(item["address_correction_fee_usd"])
                disputed_items.append({
                    "tracking": tracking,
                    "reason": "ERRONEOUS_ADDRESS_CORRECTION_SURCHARGE",
                    "refund_eligible_usd": fee
                })
                total_recovery += fee

        return {
            "total_shipments_audited": len(billed_shipments),
            "disputed_shipment_count": len(disputed_items),
            "total_claimable_refund_usd": round(total_recovery, 2),
            "claim_items": disputed_items,
            "roi_action": "SUBMIT_AUTOMATED_EDI_DISPUTE_BATCH" if total_recovery > 0 else "INVOICE_CLEAN"
        }

    @staticmethod
    def compile_carrier_gsr_refund_claim(tracking_number: str, carrier: str, disputed_charge_usd: float, claim_type: str = "LATE_DELIVERY_GSR") -> Dict[str, Any]:
        return {
            "tracking_number": tracking_number,
            "carrier": carrier.upper(),
            "claim_type": claim_type,
            "claim_amount_usd": disputed_charge_usd,
            "statutory_claim_window_days": 15,
            "submission_status": "QUEUED_FOR_CARRIER_BILLING_DISPUTE_PORTAL",
            "direct_remittance": "Credit applied directly to upcoming weekly freight invoice."
        }
