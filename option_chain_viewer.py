import streamlit as st 
import requests
import pandas as pd
import time

class OptionChain:
    def __init__(self, symbol='NIFTY', timeout=5) -> None:
        self.__url = f"https://www.nseindia.com/api/option-chain-indices?symbol={symbol}"
        self.__session = requests.Session()
        self.__session.headers.update({
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Referer": "https://www.nseindia.com/option-chain"
        })
        self.__timeout = timeout
        self.__initialize_session()

    def __initialize_session(self):
        initial_url = "https://www.nseindia.com/option-chain"
        try:
            response = self.__session.get(initial_url, timeout=self.__timeout)
            response.raise_for_status()
        except requests.exceptions.RequestException as ex:
            st.error(f"Initial session request error: {ex}")

    def fetch_data(self, expiry_date=None, starting_strike_price=None, number_of_rows=2):
        try:
            response = self.__session.get(url=self.__url, timeout=self.__timeout)
            response.raise_for_status()
            data = response.json()

            # Check and debug the structure of the JSON response
            if 'records' not in data or 'data' not in data['records']:
                st.error(f"Unexpected JSON structure: {data}")
                return pd.DataFrame(), None

            df = pd.json_normalize(data['records']['data'])

            # Filter by expiry_date and starting_strike_price if provided
            if expiry_date is not None:
                df = df[df.expiryDate == expiry_date]
                
            if starting_strike_price is not None:
                df = df[df.strikePrice >= starting_strike_price][:number_of_rows]

            # Select OI and CHNG IN OI columns for both Call and Put options
            df = df[['strikePrice', 'CE.openInterest', 'CE.changeinOpenInterest', 'PE.openInterest', 'PE.changeinOpenInterest']]
            df = df.rename(columns={
                'CE.openInterest': 'Call Open Interest', 
                'CE.changeinOpenInterest': 'Call Change in Open Interest',
                'PE.openInterest': 'Put Open Interest', 
                'PE.changeinOpenInterest': 'Put Change in Open Interest'
            })

            # Get the underlying index value
            underlying_index = data['records'].get('underlyingValue', 'N/A')

            return df, underlying_index
        except requests.exceptions.RequestException as ex:
            st.error(f"Request error: {ex}")
        except ValueError as ex:
            st.error(f"JSON decode error: {ex}")
        except KeyError as ex:
            st.error(f"Key error: {ex}")

        return pd.DataFrame(), None

def main():
    st.set_page_config(layout="wide")
    st.title("NSE Option Chain Viewer")

    symbol = st.text_input("Enter the symbol (e.g., NIFTY, BANKNIFTY):", "BANKNIFTY")
    expiry_date = st.text_input("Enter the expiry date (YYYY-MM-DD) (optional):", "")
    starting_strike_price = st.number_input("Enter the starting strike price (optional):", min_value=0, value=0)
    number_of_rows = st.number_input("Number of rows to display:", min_value=1, max_value=100, value=10)

    # Create a placeholder for the underlying index
    index_placeholder = st.empty()

    if st.button("Fetch Data"):
        with st.spinner("Fetching data..."):
            time.sleep(2)  # Delay to handle potential rate limiting or blocking
            obj = OptionChain(symbol=symbol)
            result, underlying_index = obj.fetch_data(
                expiry_date=expiry_date if expiry_date else None,
                starting_strike_price=starting_strike_price if starting_strike_price else None,
                number_of_rows=number_of_rows
            )
            if not result.empty:
                st.write(result)
                # Display the underlying index value in the top right corner
                index_placeholder.markdown(f"### Underlying Index({symbol}): {underlying_index}")
            else:
                st.write("No data available or an error occurred.")

if __name__ == '__main__':
    main()
