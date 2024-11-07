import sys
import logging

# Configure logging
logging.basicConfig(filename='Daviann_alert_action.log', level=logging.INFO)

def main():
    # Log a message when the alert action is triggered
    logging.info("Alert action triggered: This is a custom log message.")

if __name__ == "__main__":
    main()

