#!/usr/bin/env python3
"""
================================================================================
FINOTT LABS - THE PAWN'S LEVERAGE CALCULATOR (PLC)
Core Financial Engineering Module | Case Study: The Intelligent Pawn
Author: Richard Masunga Bernad (MASBER15)
Location: MUST Mbeya, Tanzania
================================================================================
Description:
    An algorithmic simulation engine that models long-term compounding asset 
    trajectories while accounting for the negative systemic drag forces of 
    inflation and hidden institutional management fees.
================================================================================
"""

import sys

def display_brand_banner():
    """
    Renders the official Masber15 Guild corporate banner layout to the 
    standard output terminal.
    """
    print("=" * 70)
    print("         ♟️  MASBER15 GUILD - THE PAWN'S LEVERAGE ENGINE v1.0.0  ♟️")
    print("       Decoding Code & Capital  |  Project: The Intelligent Pawn")
    print("=" * 70)

def safe_float_input(prompt_message, default_fallback):
    """
    Safely captures user numeric inputs via terminal. Evaluates inputs using 
    exception handling structures to prevent processing execution crashes.
    
    Args:
        prompt_message (str): The descriptive input instruction prompt.
        default_fallback (float): The default data value applied on exception.
        
    Returns:
        float: Verified numeric floating-point asset parameter.
    """
    try:
        user_raw = input(f"{prompt_message} [Default: {default_fallback}]: ").strip()
        if not user_raw:
            return default_fallback
        return float(user_raw)
    except ValueError:
        print(f"⚠️  [SYSTEM WARNING] Invalid input format. Falling back to default: {default_fallback}")
        return default_fallback

def run_simulation(principal, monthly_deposit, annual_return, fee_pct, inflation_pct, timeline_years):
    """
    Executes the underlying time-phased financial compounding algorithm loop. 
    Adjusts nominal market returns against parasitic economic drag forces.
    
    Mathematical Formulation Applied:
        Real Rate = Nominal Return Rate - Management Fees - Inflation Rate
    
    Args:
        principal (float): Initial account balance injection space.
        monthly_deposit (float): Monthly recurring resource contributions.
        annual_return (float): Projected gross annualized asset performance.
        fee_pct (float): Institutional asset management cost deductions.
        inflation_pct (float): Structural currency devaluation rate.
        timeline_years (float): Total temporal duration of execution simulation.
        
    Returns:
        tuple: (final_purchasing_power, total_out_of_pocket_capital)
    """
    # Step 1: Normalize percentage inputs into standard floating-point decimals
    nominal_return_decimal = annual_return / 100.0
    fee_decimal = fee_pct / 100.0
    inflation_decimal = inflation_pct / 100.0
    
    # Step 2: Compute net inflation-adjusted real annual rate of return 
    real_annual_return = nominal_return_decimal - fee_decimal - inflation_decimal
    
    # Step 3: Deconstruct annual rates into atomic monthly interest steps
    monthly_return_rate = real_annual_return / 12.0
    
    # Step 4: Map operational timeframe into standard monthly indexing intervals
    total_operational_months = int(timeline_years * 12)
    
    # Step 5: Initialize core tracking state variables
    running_portfolio_wealth = principal
    cumulative_invested_capital = principal

    # Step 6: Execute discrete-time monthly compilation simulation loop
    for month in range(1, total_operational_months + 1):
        # Apply incoming contribution deposit at start of compounding cycle interval
        running_portfolio_wealth += monthly_deposit
        cumulative_invested_capital += monthly_deposit
        
        # Compound the account balance balance by net real monthly asset yield scalar
        running_portfolio_wealth = running_portfolio_wealth * (1.0 + monthly_return_rate)
        
    return round(running_portfolio_wealth, 2), round(cumulative_invested_capital, 2)

def main():
    """
    Main orchestration runtime control loop for the PLC deployment application.
    """
    display_brand_banner()
    
    # --------------------------------------------------------------------------
    # DATA COLLECTION LAYER
    # --------------------------------------------------------------------------
    print("\n📥 [PARAMETER ACQUISITION] Define Asset Simulation Constraints:")
    
    starting_capital = safe_float_input("  ▶ Initial Base Principal ($)", 1000.0)
    monthly_injection = safe_float_input("  ▶ Monthly Contribution ($)", 200.0)
    expected_growth   = safe_float_input("  ▶ Nominal Annual Market Return (%)", 8.5)
    broker_fees       = safe_float_input("  ▶ Hidden Broker Management Fee (%)", 1.5)
    macro_inflation   = safe_float_input("  ▶ Estimated Inflation Rate (%)", 3.0)
    simulation_span   = safe_float_input("  ▶ Tactical Horizon Timeline (Years)", 20.0)
    
    # --------------------------------------------------------------------------
    # ALGORITHMIC PROCESSING LAYER
    # --------------------------------------------------------------------------
    final_wealth, total_out_of_pocket = run_simulation(
        starting_capital, monthly_injection, expected_growth, 
        broker_fees, macro_inflation, simulation_span
    )
    
    # --------------------------------------------------------------------------
    # ANALYSIS AND OUTPUT RENDER LAYER
    # --------------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("🎯 STRATEGIC WEALTH PROJECTION OUTCOMES")
    print("=" * 70)
    print(f" • Net Invested Out-of-Pocket Capital : ${total_out_of_pocket:,.2f}")
    print(f" • Real Future Purchasing Power       : ${final_wealth:,.2f}")
    
    # Evaluate compound interest output trajectories
    net_interest_yield = final_wealth - total_out_of_pocket
    
    if net_interest_yield > 0:
        print(f" • Net Systemic Compound Growth       : ${net_interest_yield:,.2f}")
    else:
        print(f" • Net Real Capital Asset Deficit     : ${abs(net_interest_yield):,.2f}")
        print("   [CRITICAL] System drag metrics outpaced base performance returns.")
        
    print("\n♟️  THE INTELLIGENT PAWN TACTICAL NOTE:")
    print(" Your 'Real Future Purchasing Power' factors in inflation and fees.")
    print(" A seemingly small 1.5% fee compounding over decades silently drains")
    print(" significant wealth off your board. Focus on tracking low-fee tools.")
    print("=" * 70)

if __name__ == "__main__":
    main()
