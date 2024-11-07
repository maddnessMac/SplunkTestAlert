import sys
import logging
import os

# Ensure the logs are written to a valid Splunk directory
log_directory = os.path.join(os.environ['SPLUNK_HOME'], 'var', 'log', 'splunk')
log_file = os.path.join(log_directory, 'Daviann_alert_action.log')

# Create the log directory if it doesn't exist
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Configure logging
logging.basicConfig(filename=log_file, level=logging.INFO)

def main():
    # Log a message when the alert action is triggered
    logging.info("Alert action triggered: This is a custom log message.")

if __name__ == "__main__":
    main()

