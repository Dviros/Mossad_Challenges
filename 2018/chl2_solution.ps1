$md5 = new-object -TypeName System.Security.Cryptography.MD5CryptoServiceProvider
$sha512 = new-object -TypeName System.Security.Cryptography.SHA512CryptoServiceProvider
$utf8 = new-object -TypeName System.Text.UTF8Encoding


while ($true){
    $server_hash = Invoke-RestMethod -Uri http://localhost
    write "Server hash:" $server_hash
    write "bruteforcing..."
    for ($i=0; $max=100000; $i++) {
        $hash = [System.BitConverter]::ToString($md5.ComputeHash($utf8.GetBytes($i)))
        $hash = $hash.ToLower() -replace '-', ''
        if ($hash -eq $server_hash){
            write "found it"
            write "the number is " $i
            $newhash = [System.BitConverter]::ToString($sha512.ComputeHash($utf8.GetBytes($i+"1")))
            $newhash = $newhash.ToLower() -replace '-', ''
            write "sending back to the server " $newhash
            Invoke-RestMethod -Uri http://localhost -Method Post -Body $newhash
            break
        }
    }
    Wait-Event -Timeout 5
}