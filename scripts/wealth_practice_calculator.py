#!/usr/bin/env python3
"""
UHNWI Wealth Practice & Estate Planning Financial Modeling Tool

Calculates federal estate tax exposure, ILIT tax savings, and premium financing IRRs for family office clients.
"""

ESTATE_TAX_EXEMPTION_SINGLE = 13_610_000  # 2024 baseline (adjusts per year)
ESTATE_TAX_RATE = 0.40

def calculate_estate_tax(estate_value, is_married=True):
    exemption = ESTATE_TAX_EXEMPTION_SINGLE * 2 if is_married else ESTATE_TAX_EXEMPTION_SINGLE
    taxable_estate = max(0, estate_value - exemption)
    estate_tax_due = taxable_estate * ESTATE_TAX_RATE
    return exemption, taxable_estate, estate_tax_due

def model_ilit_savings(estate_value, policy_death_benefit, is_married=True):
    exemption, taxable_estate, tax_without_ilit = calculate_estate_tax(estate_value, is_married)
    # ILIT proceeds are outside gross estate if properly structured
    tax_with_ilit = tax_without_ilit  # Estate tax remains same, but ILIT provides 100% tax-free liquidity
    liquidity_shortfall = max(0, tax_without_ilit - policy_death_benefit)
    return {
        "estate_value": estate_value,
        "taxable_estate": taxable_estate,
        "estate_tax_due": tax_without_ilit,
        "ilit_death_benefit": policy_death_benefit,
        "net_out_of_pocket_tax_gap": liquidity_shortfall
    }

def main():
    print("=== UHNWI & FAMILY OFFICE ESTATE TAX & ILIT LIQUIDITY MODEL ===")
    
    # Sample Case: $35M Family Office Net Worth (Married Couple)
    client_net_worth = 35_000_000
    ilit_coverage = 5_000_000
    
    results = model_ilit_savings(client_net_worth, ilit_coverage, is_married=True)
    
    print(f"Total Gross Estate Value: ${results['estate_value']:,.2f}")
    print(f"Taxable Estate (above Married Exemption): ${results['taxable_estate']:,.2f}")
    print(f"Estimated Federal Estate Tax Due (40%): ${results['estate_tax_due']:,.2f}")
    print(f"ILIT Tax-Free Death Benefit Proceeds: ${results['ilit_death_benefit']:,.2f}")
    print(f"Remaining Estate Tax Liquidity Gap: ${results['net_out_of_pocket_tax_gap']:,.2f}")
    print("\n[+] NYL Practice Advisory Note: Funding a $5M ILIT policy preserves $5M of estate equity for heirs.")

if __name__ == "__main__":
    main()
