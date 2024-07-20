# NSE Option Chain Viewer

This project is a Streamlit application that fetches and displays the NSE (National Stock Exchange) option chain data for a specified symbol (e.g., NIFTY, BANKNIFTY). The application allows users to input various parameters such as the symbol, expiry date, starting strike price, and the number of rows to display. It also shows the underlying index value in the top right corner, which updates in real time according to the symbol entered.

## Features

- Fetches option chain data from the NSE website.
- Displays Call and Put option open interest (OI) and change in open interest (CHNG IN OI).
- Allows filtering by expiry date and starting strike price.
- Displays the underlying index value in real-time.

## Requirements

- Python 3.7+
- Streamlit
- Requests
- Pandas

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Bishwarup-Das/Option-Chain-Viewer.git
    cd Option-Chain-Viewer
    ```

2. Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    streamlit run main.py
    ```

## Usage

1. Enter the symbol (e.g., NIFTY, BANKNIFTY) in the input box.
2. Optionally, enter the expiry date in YYYY-MM-DD format.
3. Optionally, enter the starting strike price.
4. Specify the number of rows to display.
5. Click the "Fetch Data" button.

The application will fetch and display the option chain data, showing the OI and CHNG IN OI for both Call and Put options. The underlying index value will be displayed in the top right corner and updated in real time.

## Code Overview

### `OptionChain` Class

- **`__init__(self, symbol='NIFTY', timeout=5)`**: Initializes the OptionChain object with the specified symbol and timeout.
- **`__initialize_session(self)`**: Initializes the session with the required headers.
- **`fetch_data(self, expiry_date=None, starting_strike_price=None, number_of_rows=2)`**: Fetches the option chain data from the NSE website and returns it as a DataFrame along with the underlying index value.

### `main` Function

- **Layout Configuration**: Sets the page layout to wide using `st.set_page_config(layout="wide")`.
- **User Inputs**: Provides input boxes for symbol, expiry date, starting strike price, and number of rows to display.
- **Fetch Data Button**: Fetches and displays the option chain data when clicked.
- **Underlying Index Placeholder**: Displays the underlying index value in the top right corner.

## Further Development

### Error Handling

- Improve error handling to provide more detailed error messages and handle specific exceptions more gracefully.
- Implement retry logic for network requests to handle transient errors.

### UI Enhancements

- Add more user-friendly UI elements such as dropdowns for expiry dates.
- Implement pagination for displaying large datasets.

### Additional Features

- Provide more filtering options, such as filtering by specific strike prices.
- Include historical data for analysis.
- Add a caching mechanism to reduce the number of network requests and improve performance.

### Testing

- Implement unit tests for the `OptionChain` class and other functions.
- Set up continuous integration to automate testing and deployment.

### Documentation

- Create detailed documentation for each function and class.
- Add examples and use cases to the README file.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

By following this README, developers should be able to set up, run, and contribute to the NSE Option Chain Viewer project. Feel free to modify and enhance the application as needed. Happy coding!
