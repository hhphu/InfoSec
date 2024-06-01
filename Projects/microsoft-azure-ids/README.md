-----
## SIGN UP IPGEOLOCATION
-----
- Go to the following website and sign up for a free member https://ipgeolocation.io/
- Obtain the API key and put it into the PowerShell Script.

-----
## CREATE VIRTUAL MACHINE
-----
- Create a new Resource Group
- Within the group, create a new Windows Virtual machine.
- Set up a username and password for RDP.
- Add a security rule that allows all inbound traffics from any sources to any ports, with any protocol

-----
## CONFIGURE SECURITY CENTER
----
- Go to `Home > Microsoft Defender for Cloud | Workload protections > Getting Started >` to turn on `Servers` option and turn off the others. 

![defender-plan.png](https://miro.medium.com/v2/resize:fit:720/format:webp/1*a2S6tj8EWxDIeKq8kIIx_Q.png)

-----
## SET UP LOG ANALYTICS WORKSTATION
-----
- Create a new Log Analytics workspace

![create-analytic-log-workspace.png](https://miro.medium.com/v2/resize:fit:720/format:webp/1*yyyaaW7PBn28EJB7ixIJUQ.png)

### CREATE DATA COLLECTION RULE
-----
- Go to `Home > Log Analytics workspaces > $WORKSPACE_NAME > Data Collection Rules >`
- Create a new Data collection rule for the resource

![create-data-collection-rule.png](https://miro.medium.com/v2/resize:fit:720/format:webp/1*U8dCk6nebz8Pc4hacmWWHA.png)

- Connect Log Analytics Workspace to the Virtual machine
	Go to `Home > Log Analytics workspaces > $WORKSPACE_NAME | Virtual machines`. Select the VM and click connect

-----
## CREATE AZURE SENTINELS
-----
- Go to Azure Sentinels and connect to the current Log Analytics Workspace

-----
## CONNECT TO VIRTUAL MACHINE
----
- Turn off firewall on VM
	- `Windows Defender Firewall > Advanced Settings > Windows Defender Firewall Properties` and turn off firewalls for Domain profile, Private profile and Public profile
- Down load the [PS script](https://github.com/hhphu/InfoSec/blob/main/Scripts/Microsoft%20Azure%20SIEM/GetEventLogs.ps1) to run on the Virtual Machine. This will catch all failed RDP attempts and store in a file called **FailedRDP.log**

![Run-Get-EventsLogs.png](https://miro.medium.com/v2/resize:fit:720/format:webp/1*Z8Y4wLmIOaxLbcAe2OYGiw.png)

-----
## CONFIGURE LOG ANALYTICS WORKSPACE TO GATHER LOGS
-----
- We need to tell LAW where to gather logs from the virtual machine
	1. `Home > $LOG_ANALYTICS_WORKSPACE`, select `Tables > Create > New custom log (MMA-based)`
	2. Upload the sample log file (which can be acquired by running the script on VM)
	3. Proceed to **Collection Path**. Here, select `Type=Windows` & `Path=C:\Users\greenman\Desktop\FailedRDP.log` (full path to the output logfile on VM)
	4. Name the custom log rule and create
- To test the newly created custom log, go to `Logs` tab under the Log Analytics Workspace. ( Note: Need to wait about 15-20' to finish the creation)
	- Input the name of the newly created custom log
	- Click Run
	- There should be output similar to the one from VM.

-----
## SET UP SENTINELS  
-----
- Run the following query to retrieve and extract values from RawData column.

```bash
FAILED_RDP_LOGINS_CL 
# split RawData into an array called splitted: latitude:931,longtitude:02651,etc.
| project splitted=split(RawData,',')
# Assign names for new columns: Latitude=latitude:931, Longtitude=longtitude:02651,etc.
| mv-expand Latitude=splitted[0],Longtitude=splitted[1], DestinationHost=splitted[2], Username=splitted[3], SourceHost=splitted[4], Country=splitted[6],Label=splitted[7]
# Extract values for columns: Latitude=931, Longtitude=02651, etc.
| mv-expand Latitude=split(Latitude,':')[1],Longtitude=split(Longtitude,':')[1], DestinationHost=split(DestinationHost,':')[1],SourceHost=split(SourceHost,':')[1],
    Country=split(Country,':')[1], Label=split(Label,':')[1], Username=split(Username,':')[1]
# Display everything but the original array.
| project-away splitted 
``` 

Query for Sentinels
```bash
FAILED_RDP_LOGINS_CL

| project splitted=split(RawData, ',')
| mv-expand Latitude=splitted[0], Longtitude=splitted[1], DestinationHost=splitted[2], Username=splitted[3], SourceHost=splitted[4], Country=splitted[6], Label=splitted[7]
| mv-expand Latitude=split(Latitude, ':')[1], Longtitude=split(Longtitude, ':')[1], DestinationHost=split(DestinationHost, ':')[1], SourceHost=split(SourceHost, ':')[1], Country=split(Country, ':')[1], Label=split(Label, ':')[1], Username=split(Username, ':')[1]
# count the number of occurences and store it in event_count variable. This will be used for Sentinels map
| summarize event_count = count() by tostring(SourceHost), tostring(Latitude), tostring(Longtitude), tostring(Country), tostring(Label), tostring(DestinationHost)
# filter out those sample logs
| where DestinationHost != "samplehost"
```

NOTE: After completion, I found other queries that achieve the same results
```bash
FAILED_RDP_WITH_GEO_CL | extend RawData = tostring(RawData) | parse RawData with * "latitude:" latitude ",longitude:" longitude ",destinationhost:" destinationhost ",username:" username ",sourcehost:" sourcehost ",state:" state ", country:" country ",label:" label ",timestamp:" timestamp | summarize event_count=count() by sourcehost, latitude, longitude, label, destinationhost, country | where sourcehost != ""
```

- Select displaying data by Maps and play around with the Map settings. Here's is an example of my map settings

![map-settings1](https://miro.medium.com/v2/resize:fit:640/format:webp/1*OjoszS6S0LgS-Sda9jyaKw.png)

![map-settings2](https://miro.medium.com/v2/resize:fit:640/format:webp/1*NXp1ewJZS_jjy1gaiL8DcA.png)

-----
## ACCOMPLISHMENTS - LESSON LEARNED - SKILLS GAINED 
-----
- Established an Azure Virtual Windows machine, accessible to the public, with enabled RDP connections, providing secure and efficient remote access capabilities.
- Developed a robust PowerShell script to retrieve Failed Logon Events (4625) from the virtual machine, integrating with a third-party API to extract geolocation data for comprehensive analysis.
- Configured an Azure Log Analytics Workspace to seamlessly ingest and manage custom logs generated within the virtual machine, enhancing visibility and monitoring capabilities.
- Utilized the powerful Kusto Query Language (KQL) to extract precise geo-data, including latitude, longitude, and country, from the logs, enabling in-depth analysis and correlation with security events.
- Integrated the extracted geo-data into Azure Sentinel, Microsoft's cloud-based Security Information and Event Management (SIEM) solution, creating a visually compelling workbook that showcases attempted attacks on a world map, providing valuable insights into attack patterns and their geographical distribution.
