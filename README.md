<h1>SplunkTestAlert</h1>

<p><strong>SplunkTestAlert</strong> is a custom Splunk app that demonstrates how to create a modular alert action, <code>log_to_file</code>, which logs messages to a file whenever an alert is triggered.</p>

<h2>Table of Contents</h2>
<ul>
  <li><a href="#overview">Overview</a></li>
  <li><a href="#features">Features</a></li>
  <li><a href="#installation">Installation</a></li>
  <li><a href="#configuration">Configuration</a></li>
  <li><a href="#usage">Usage</a></li>
  <li><a href="#troubleshooting">Troubleshooting</a></li>
  <li><a href="#contributing">Contributing</a></li>
  <li><a href="#license">License</a></li>
</ul>

<h2 id="overview">Overview</h2>
<p>The <strong>SplunkTestAlert</strong> app provides an example of a custom alert action that can be used in Splunk alerts. When the <code>log_to_file</code> alert action is triggered, it logs a message to a specified file with details of the alert.</p>
<h3>Directory Structure</h3>
<pre>
$SPLUNK_HOME/etc/apps/SplunkTestAlert/
├── default
│   ├── alert_actions.conf
│   └── app.conf
├── bin
│   └── log_to_file.py
└── metadata
    └── default.meta
</pre>

<h2 id="features">Features</h2>
<ul>
  <li><strong>Custom Alert Action</strong>: <code>log_to_file</code> writes a log message to a specified file each time the alert triggers.</li>
  <li><strong>Simple Logging Mechanism</strong>: Logs the payload and alert metadata for easy monitoring.</li>
  <li><strong>Scheduled Alert Example</strong>: A test alert is configured to trigger periodically for demonstration purposes.</li>
</ul>

<h2 id="installation">Installation</h2>
<ol>
  <li><strong>Clone the Repository</strong>:
    <pre><code>git clone https://github.com/your-username/SplunkTestAlert.git</code></pre>
  </li>
  <li><strong>Move the App to Your Splunk Directory</strong>:
    <p>Place the <code>SplunkTestAlert</code> directory in the <code>$SPLUNK_HOME/etc/apps/</code> folder.</p>
    <pre><code>mv SplunkTestAlert $SPLUNK_HOME/etc/apps/</code></pre>
  </li>
  <li><strong>Restart Splunk</strong>:
    <pre><code>splunk restart</code></pre>
  </li>
</ol>

<h2 id="configuration">Configuration</h2>

<h3>File Structure</h3>
<p>The main configuration files include:</p>
<ul>
  <li><code>alert_actions.conf</code>: Configures the custom alert action.</li>
  <li><code>savedsearches.conf</code>: Contains a sample scheduled search to demonstrate the <code>log_to_file</code> alert.</li>
  <li><code>app.conf</code>: Basic app metadata and visibility settings.</li>
  <li><code>bin/log_to_file.py</code>: Python script that performs the log action when the alert triggers.</li>
</ul>

<h3>Alert Action Script</h3>
<ul>
  <li><strong>Script Location</strong>: The alert action script (<code>log_to_file.py</code>) should be located in the <code>bin</code> folder.</li>
  <li><strong>Permissions</strong>: Ensure the script is executable:
    <pre><code>chmod +x $SPLUNK_HOME/etc/apps/SplunkTestAlert/bin/log_to_file.py</code></pre>
  </li>
</ul>

<h2 id="usage">Usage</h2>
<ol>
  <li><strong>Create or Modify Alerts</strong>:
    <p>Use the sample alert provided in <code>savedsearches.conf</code> or create a new alert in Splunk and configure it to use the <code>log_to_file</code> action.</p>
  </li>
  <li><strong>Trigger the Alert</strong>:
    <p>When the alert conditions are met, the <code>log_to_file</code> action will execute, logging a message to the specified file.</p>
  </li>
  <li><strong>Check the Log Output</strong>:
    <p>Verify that messages are being logged as expected in the specified log file.</p>
  </li>
</ol>

<h2 id="troubleshooting">Troubleshooting</h2>
<ul>
  <li><strong>Script Not Found</strong>: If you encounter a <code>script not found</code> error, ensure the script name matches the alert action name (<code>log_to_file</code>) and that it’s placed in the <code>bin</code> directory.</li>
  <li><strong>Permission Issues</strong>: Ensure that <code>log_to_file.py</code> has executable permissions.</li>
  <li><strong>Logging Path</strong>: Double-check the log file path in the script and ensure Splunk has write permissions for that location.</li>
</ul>

<h2 id="contributing">Contributing</h2>
<p>Contributions are welcome! If you’d like to add features or improvements, feel free to fork the repository and submit a pull request.</p>

<h2 id="license">License</h2>
<p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>
