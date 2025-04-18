from src.settings import DATA_PATH, logger
import pandas as pd
from typing import List
import os


# Temporary for VCBF funds
try:
    logger.debug("Loading fund portfolios data from JSON file.")
    path = os.path.join(DATA_PATH, "VCBF/fund_portfolios.csv")
    FUND_DF = pd.read_csv(path)
    FUND_DF["Date"] = pd.to_datetime(FUND_DF["Date"], format="%Y-%m-%d")
    logger.info(
        f"Fund portfolios data loaded successfully with {len(FUND_DF)} rows.")
except Exception as e:
    logger.error(f"Failed to load fund portfolios data: {e}")
    FUND_DF = pd.DataFrame()  # Fallback to an empty DataFrame

# Load financial data
try:
    logger.debug("Loading financial data from JSON file.")
    path = os.path.join(DATA_PATH, "financial_data.csv")
    FINANCIAL_DF = pd.read_csv(path)
    logger.info(
        f"Financial data loaded successfully with {len(FINANCIAL_DF)} rows.")
except Exception as e:
    logger.error(f"Failed to load financial data: {e}")
    FINANCIAL_DF = pd.DataFrame()


def get_stocks_list() -> List[str]:
    """
    Get the list of stock symbols
    """
    try:
        # logger.info("Fetching the list of stock symbols.")
        stock_list = FUND_DF["Category"].unique().tolist()
        logger.debug(f"Retrieved {len(stock_list)} unique stock symbols.")
        return stock_list
    except KeyError as e:
        logger.error(f"Failed to fetch stock symbols: {e}")
        return []
