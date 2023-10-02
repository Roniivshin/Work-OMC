function change-mail-on-monitor {
    # Set the error action preference to SilentlyContinue
    $ErrorActionPreference = "SilentlyContinue"
    Copy-Item C:\testAlexeym\Ronii\AddMail\changemailonmonitor.txt.bak C:\testAlexeym\Ronii\AddMail\changemailonmonitor.txt -ErrorAction Ignore
    Set-Location "C:\Program Files (x86)\PuTTY"

    do {
        $connStatus = ""
        $pwMon = ""

        while (!$pwMon) {
            Write-Host "Please enter ROOT password for monitor.omc.co.il - " -ForegroundColor Green -NoNewline
            Write-Host " -foreground Yellow -backgroundcolor Black -nonewline"
            $pwMon = Read-Host " " -AsSecureString
            $pwMon = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($pwMon))
        }
        m
        Write-Host "Checking SSH connection..."
        $connStatus = echo y | .\plink.exe -ssh -l root -pw $pwMon monitor.omc.co.il -nc monitor.omc.co.il:22 | Select-Object -Last 2
    }
    until ($connStatus -like '*SSH*')

    echo "Password is OK."

    $checkVar = Read-Host "Enter full prefix or email adress "

    while (!$checkVar) {
        Write-Host "`nNo search entered." -ForegroundColor Red
        Write-Host "Enter full prefix or email address" -NoNewLine -ForegroundColor Green
        $checkVar = Read-Host " "
    }

    $newContact = Read-Host "Enter new contact: "

    while (!$newContact) {
        Write-Host "`nNo VM entered." -ForegroundColor Red
        Write-Host "Enter full prefix or email address" -NoNewLine -ForegroundColor Green
        $newContact = Read-Host " "
    }

     $fileNameMon = "C:\testAlexeym\Ronii\AddMail\changemailonmonitor.txt"
    (Get-Content $fileNameMon) -replace  "CheckVar" , $checkVar| Set-Content $fileNameMon
    (Get-Content $fileNameMon) -replace "newContact" , $newContact | Set-Content $fileNameMon

    echo "y" | .\plink.exe -ssh -l root -pw $pwMon monitor.omc.co.il -m $fileNameMon
}
