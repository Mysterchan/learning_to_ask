import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_gold_demand_by_country(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "returns realtime gold demand by country"
    
    """
    url = f"https://global-economy-analytics.p.rapidapi.com/golddemandbycountryinounces"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-economy-analytics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_all_country_energy(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns realtime energy consumption for current year YTD in BTUS(Billion BTU`s) Top 10 countries and world total"
    
    """
    url = f"https://global-economy-analytics.p.rapidapi.com/countryenergy"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-economy-analytics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_specific_country_economic_stats_forecast_news(specficcountry: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This specific country endpoint returns top 30 countries:
		
		Realtime Economic states: population, national debt, GDP, public debt to gdp ratio, external debt to gdp ratio
		
		Economic summary: economic forecast YTD, economic outlook
		
		Realtime latest economic news: top ten latest articles, various sources"
    
    """
    url = f"https://global-economy-analytics.p.rapidapi.com/country/{specficcountry}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-economy-analytics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_gold_holding_all_countires(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "returns gold Holding By Country In Ounces"
    
    """
    url = f"https://global-economy-analytics.p.rapidapi.com/goldholdingbycountryinounces"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-economy-analytics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_type_of_gold_production(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This realtime endpoint returns the amount of gold recycled, and gold produced in ounces."
    
    """
    url = f"https://global-economy-analytics.p.rapidapi.com/goldproduction"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-economy-analytics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_world_energy_production(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This realtime endpoint returns world energy production for the most used resources YTD"
    
    """
    url = f"https://global-economy-analytics.p.rapidapi.com/worldenergyproduction"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-economy-analytics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_world_total_gold_demand_supply_in_ounces(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This realtime endpoint returns the amount of gold Demand Supply YTD since 2012."
    
    """
    url = f"https://global-economy-analytics.p.rapidapi.com/totalgolddemandsupplyinounces"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-economy-analytics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_us_workforce_demographics(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This realtime endpoint returns the amount of US Income Taxpayers, Us Workforce (Now and 2000), US Official Unemployed, US Actual Unemployment, US Private Sector Jobs, US Self Employed, US Not In Labor Force(Now and 2000), US Full Time Workers, US Part Time Workers, US Union Workers, US Government Employees, US Median Income(Now 2000), US Median New Home(Now AND 2000), and US Manufacturing Jobs(Now and 2000)."
    
    """
    url = f"https://global-economy-analytics.p.rapidapi.com/workerinfo"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-economy-analytics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_us_new_home_sales_annual_rate(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This realtime endpoint returns the new Home Sales Annual Rate since 2007"
    
    """
    url = f"https://global-economy-analytics.p.rapidapi.com/newhomesalesannualrate"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-economy-analytics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_dollar_to_important_good_ratio(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This realtime endpoint gets the current ratios of Dollar to Oil Ratio Now, Dollar to Oil Ratio 1913, Dollar to Silver Ratio Now, Dollar to Silver Ratio 1913, Dollar to Gold Ratio Now, Dollar to Gold Ratio 1913, Paper to Silver Ratio Now, Paper to Gold Ratio Now, Dollar to Crypto Ratio Now, and Dollar to Crypto Ratio 2013"
    
    """
    url = f"https://global-economy-analytics.p.rapidapi.com/moneytoproductratio"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-economy-analytics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_world_metal_production_change(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This realtime endpoint returns the world production change of metals:
		Gold, Silver, Platinum, Palladium, Lithium, Nickel, Titanium, Zinc, Manganese, Copper, Aluminum, and Iron"
    
    """
    url = f"https://global-economy-analytics.p.rapidapi.com/productionchangesince2000"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-economy-analytics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_world_precious_metal_reserves(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This realtime endpoint returns the amount of precious metals in the World:
		Gold, Silver, Platinum, Palladium, Lithium, Nickel, Titanium, Zinc, Manganese, Copper, Aluminum, and Iron"
    
    """
    url = f"https://global-economy-analytics.p.rapidapi.com/preciousmetalreserves"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-economy-analytics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_us_money_creation_and_circulation(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This realtime endpoint returns details of money and circulation in the US Economy:
		US Treasury Dollars(Now and 2000), US M2 Money Supply(Now and 2000), and Currency and Derivatives(Now and 2000)"
    
    """
    url = f"https://global-economy-analytics.p.rapidapi.com/moneycreation"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-economy-analytics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_us_liabilities(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This realtime endpoint returns the largest US liabilities:
		US Social Security Liability, US Medicare Liability, US Unfunded Liability, and US Liability Per Citizen"
    
    """
    url = f"https://global-economy-analytics.p.rapidapi.com/liability"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-economy-analytics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_us_largest_budget_items(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This realtime endpoint returns the largest budget items for the US Government:
		US Medicaid/Medicaid, US Social Security, US Defense, and US Liability Per Citizen"
    
    """
    url = f"https://global-economy-analytics.p.rapidapi.com/largestbudgetitem"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-economy-analytics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_us_demography_on_quality_of_life(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This realtime endpoint returns the amount of US Bankruptcies, US Foreclosures, US Poverty, US people living without insurance, US retirees, US Retirees, US Disabled, US Disabled, US Medicare Enrollees, US Medicaid Recipients, US Millionaires, US Food Stamp Recipients, and US Population."
    
    """
    url = f"https://global-economy-analytics.p.rapidapi.com/uspopqualityoflifestats"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-economy-analytics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_us_energy_consumption(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This realtime endpoint returns the type of energy resource usage in the US IN BTUS YTD:
		Natural Gas, Crude Oil, Coal, Nuclear, Biomass, Wind, Hydroelectric, Biofuels, Solar, Geothermal, and Total"
    
    """
    url = f"https://global-economy-analytics.p.rapidapi.com/usenergyconsumption"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-economy-analytics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_us_new_home_median_sale_price(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This realtime endpoint returns new Home Median Sale Price since 2007"
    
    """
    url = f"https://global-economy-analytics.p.rapidapi.com/newhomemediansaleprice"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-economy-analytics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_us_existing_home_median_sale_price(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This realtime endpoint returns existing Home Median Sale Price"
    
    """
    url = f"https://global-economy-analytics.p.rapidapi.com/existinghomemediansaleprice"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-economy-analytics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_us_new_housing_starts_annual_rate(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This realtime endpoint returns new Housing Starts Annual Rate since 2007"
    
    """
    url = f"https://global-economy-analytics.p.rapidapi.com/newhousingstartsannualrate"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-economy-analytics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_us_existing_home_sales_annual_rate(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This realtime endpoint returns the existing Home Sales Annual Rate since 2007"
    
    """
    url = f"https://global-economy-analytics.p.rapidapi.com/existinghomesalesannualrate"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-economy-analytics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_gold_per_sector(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This realtime endpoint returns Gold Demand By Sector In Ounces"
    
    """
    url = f"https://global-economy-analytics.p.rapidapi.com/golddemandbysectorinounces"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-economy-analytics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_us_trade_balance(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This realtime endpoint returns US Debt Held By Foreign Countries,  US Trade Deficit, US Trade Deficit China, and US Imported Oil"
    
    """
    url = f"https://global-economy-analytics.p.rapidapi.com/ustradebalance"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-economy-analytics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_us_national_debt_statistics(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This realtime endpoint returns US National Debt, US National Debt Per Citizen, US National Debt Per Taxpayer, US Federal Official Spending, US Federal Budget Deficit Official, US Federal Actual Spending, US Federal Budget Deficit Actual, US State Debt, US Local Debt, US State Debt Per Citizen, US Local Debt Per Citizen, and US Total Debt To GDP Ratio"
    
    """
    url = f"https://global-economy-analytics.p.rapidapi.com/usnationaldebt"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-economy-analytics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_us_auto_sales_ytd(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "this endpoint returns the number of US car sales of 34 major auto brands"
    
    """
    url = f"https://global-economy-analytics.p.rapidapi.com/autosales"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-economy-analytics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_us_assets(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This realtime endpoint returns Household Assets, US Total National Assets,  and assets Per Citizen"
    
    """
    url = f"https://global-economy-analytics.p.rapidapi.com/usassets"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-economy-analytics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_us_unfunded_debt_interest(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This realtime endpoint returns US Total Interest Paid, US Interest Per Adult, US Bank Interest Received, US Bank Interest Paid,  US Student Loan Debt, US Student Loan Debt Per Student, US Credit Card Debit, US Total Debt, US Total Personal Debt US Savings Per Family, and US Personal Debt Per Citizen"
    
    """
    url = f"https://global-economy-analytics.p.rapidapi.com/usunfundeddebt&interest"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-economy-analytics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_us_federal_debt_to_gdp_ratio_history(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This realtime endpoint returns US Federal Debt To GDP Ratio (1960, 1980, 2000, NOW)"
    
    """
    url = f"https://global-economy-analytics.p.rapidapi.com/usfederaldebttogdpratio"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-economy-analytics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_us_spending(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This realtime endpoint returns US Total Federal Spending, and Spending To GDP."
    
    """
    url = f"https://global-economy-analytics.p.rapidapi.com/usspending"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-economy-analytics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_us_tax_revenue_statistics(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This realtime endpoint returns US Federal Tax Revenue, US Revenue Per Citizen, US Income Tax Revenue, US Payroll Tax Revenue, US CorporateTax Revenue, US Total State Revenue, US Total Local Revenue,   US Tariff Tax Revenue, and US GDP"
    
    """
    url = f"https://global-economy-analytics.p.rapidapi.com/ustaxrevenue"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-economy-analytics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_all_country_economic_stats_forecast_news(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This ALL countries endpoint returns top 30 countries:
		
		Realtime Economic states: population, national debt, GDP, public debt to gdp ratio, external debt to gdp ratio
		
		Economic summary: economic forecast YTD, economic outlook
		
		Realtime latest economic news: top ten latest articles, various sources"
    
    """
    url = f"https://global-economy-analytics.p.rapidapi.com/countries"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-economy-analytics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_all_us_state_economic_stats(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This All state endpoint returns: 
		
		Demographics: realtime population, unemployment count, food stamp recipient count.
		Economic Data: GDP, debt, debt to GDP ratio, in state revenue, spending, debt per citizen"
    
    """
    url = f"https://global-economy-analytics.p.rapidapi.com/allstates"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-economy-analytics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_specific_state_economic_stats_abbreviations(stateabbreviations: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This specific state endpoint returns: 
		
		Demographics: realtime population, unemployment count, food stamp recipient count.
		Economic Data: GDP, debt, debt to GDP ratio, in state revenue, spending, debt per citizen"
    
    """
    url = f"https://global-economy-analytics.p.rapidapi.com/states/abbreviations/{stateabbreviations}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-economy-analytics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_specific_state_economic_stats(specificstate: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This specific state endpoint returns: 
		
		Demographics: realtime population, unemployment count, food stamp recipient count.
		Economic Data: GDP, debt, debt to GDP ratio, in state revenue, spending, debt per citizen"
    
    """
    url = f"https://global-economy-analytics.p.rapidapi.com/states/{specificstate}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-economy-analytics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

