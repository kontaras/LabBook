# Environment variables
Get: `$env:<VAR>`  
Set: `$env:<VAR> = "<VALUE>"` **The " matters**

# Freeing up a port
`taskkill /pid (Get-NetTCPConnection -LocalPort <PORT>).OwningProcess /f`

# Edit profile
`notepad $PROFILE`

# Enable bash-like completion
`Set-PSReadlineKeyHandler -Key Tab -Function Complete`
