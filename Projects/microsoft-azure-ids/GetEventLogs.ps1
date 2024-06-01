#######################################################################################################################################################################################
### This PowerShell is written to retrieve Windows Event Failed Logons logs. Logs will be retrieved, reformated and fetched to Microsoft Azure Sentinels for analysis.              ###
### This script is part of my Microsoft Azure Infrastructure Monintoring and Threat Analysis.                                                                                       ###
### Details of the project can be found here: https://www.hqphu.com/posts/6kAWd9Mm6i9jXrkiE90tct                                                                                    ###
#######################################################################################################################################################################################


$API_KEY = <API_KEY>
$LOG_FILE_NAME = "FailedRDP.log"
$LOG_FILE_PATH = <PATH_TO_$($LOG_FILE_NAME)>
$SAMPLE_LOGS = @(
    "latitude:47.91542,longitude:-120.60306,destinationhost:samplehost,username:fakeuser,sourcehost:24.16.97.222,state:Washington,country:United States,label:United States - 24.16.97.222,timestamp:2021-10-26 03:28:29",
    "latitude:-22.90906,longitude:-47.06455,destinationhost:samplehost,username:lnwbaq,sourcehost:20.195.228.49,state:Sao Paulo,country:Brazil,label:Brazil - 20.195.228.49,timestamp:2021-10-26 05:46:20",
    "latitude:52.37022,longitude:4.89517,destinationhost:samplehost,username:CSNYDER,sourcehost:89.248.165.74,state:North Holland,country:Netherlands,label:Netherlands - 89.248.165.74,timestamp:2021-10-26 06:12:56",
    "latitude:40.71455,longitude:-74.00714,destinationhost:samplehost,username:ADMINISTRATOR,sourcehost:72.45.247.218,state:New York,country:United States,label:United States - 72.45.247.218,timestamp:2021-10-26 10:44:07",
    "latitude:33.99762,longitude:-6.84737,destinationhost:samplehost,username:AZUREUSER,sourcehost:102.50.242.216,state:Rabat-Sal�-K�nitra,country:Morocco,label:Morocco - 102.50.242.216,timestamp:2021-10-26 11:03:13",
    "latitude:-5.32558,longitude:100.28595,destinationhost:samplehost,username:Test,sourcehost:42.1.62.34,state:Penang,country:Malaysia,label:Malaysia - 42.1.62.34,timestamp:2021-10-26 11:04:45",
    "latitude:41.05722,longitude:28.84926,destinationhost:samplehost,username:AZUREUSER,sourcehost:176.235.196.111,state:Istanbul,country:Turkey,label:Turkey - 176.235.196.111,timestamp:2021-10-26 11:50:47",
    "latitude:55.87925,longitude:37.54691,destinationhost:samplehost,username:Test,sourcehost:87.251.67.98,state:null,country:Russia,label:Russia - 87.251.67.98,timestamp:2021-10-26 12:13:45",
    "latitude:52.37018,longitude:4.87324,destinationhost:samplehost,username:AZUREUSER,sourcehost:20.86.161.127,state:North Holland,country:Netherlands,label:Netherlands - 20.86.161.127,timestamp:2021-10-26 12:33:46",
    "latitude:17.49163,longitude:-88.18704,destinationhost:samplehost,username:Test,sourcehost:45.227.254.8,state:null,country:Belize,label:Belize - 45.227.254.8,timestamp:2021-10-26 13:13:25",
    "latitude:-55.88802,longitude:37.65136,destinationhost:samplehost,username:Test,sourcehost:94.232.47.130,state:Central Federal District,country:Russia,label:Russia - 94.232.47.130,timestamp:2021-10-26 14:25:33"
)


$EventFilter = @'
    <QueryList>
        <Query Id="0" Path="Security">
            <Select Path="Security">
                *[System[(EventID='4625')]]
            </Select>
        </Query>
    </QueryList>
'@

################################################ FUNCTIONS SECTION ################################################

Function Write-Sample-Log() {
    foreach($sample_log in $SAMPLE_LOGS) {
        $sample_log | Out-File $LOG_FILE_PATH -Append -Encoding utf8
    }
    
}

Function Retrieve-Logs() {
    $events = Get-WinEvent -FilterXml $EventFilter -ErrorAction SilentlyContinue 
    return $events
}

Function Extract-Logs-Data() {
    param ($Events)
    foreach ($event in $Events)
    {
        $year = $event.TimeCreated.Year
        $month = $event.TimeCreated.Month
        $day = $event.TimeCreated.Day
        $hour = $event.TimeCreated.Hour
        $minute = $event.TimeCreated.Minute
        $second = $event.TimeCreated.Second
        $timestamp = "$($year)-$($month)-$($day) $($hour):$($minute):$($second)"
        
        $log_contents = Get-Content -Path $LOG_FILE_PATH
        if (-Not ($log_contents -match "$($timestamp)") -or ($log_contents.Length -eq 0)){
            Retrieve-API-Response $event $timestamp
        }
    }
}

Function Retrieve-API-Response($event,$timestamp) {

    # Index 5: Account Name (Attempted logon)
    # Index 13: Work Station Name (Source)
    # Index 19: IP Address
    
    $eventID = $event.Id
    $destination =$event.MachineName
    $username = $event.properties[5].Value
    $source = $event.properties[13].Value
    $ip = $event.properties[19].Value
    

    $API_ENDPOINT = "https://api.ipgeolocation.io/ipgeo?apiKey=$($API_KEY)&ip=$($ip)"
    $response = Invoke-WebRequest -UseBasicParsing -Uri $API_ENDPOINT


    # Pull Data from API response and store them in variables
    $responseData = $response.Content | ConvertFrom-Json
    $latitude = $responseData.latitude
    $longitude = $responseData.longitude
    $state_prov = $responseData.state_prov
    if ($state_prov -eq "") {$state_prov = "null"}
    $country = $responseData.country_name
    if ($country -eq "") {$country = "null"}
    

    # Append log to the log file
    $new_log = "latitude:$($latitude),longitude:$($longitude),destinationhost:$($destination),username:$($username),sourcehost:$($source),state:$($state_prov), country:$($country),label:$($country) - $($ip),timestamp:$($timestamp)" 
    $new_log | Out-File $LOG_FILE_PATH -Append -Encoding utf8
    Write-Host -BackgroundColor Black -ForegroundColor Green $new_log 

}


################################################ EXECUTION SECTION ################################################
# Create a log file if it doesn't exist
if ((Test-Path $LOG_FILE_PATH) -eq $false) {
    New-Item -ItemType File -Path $LOG_FILE_PATH
    Write-Sample-Log
}

while ($true) { 
    Start-Sleep -Seconds 2
    $Events = Retrieve-Logs

    Extract-Logs-Data($Events)
}

