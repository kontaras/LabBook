# Environment variables
Get: `$env:<VAR>`  
Set: `$env:<VAR> = "<VALUE>"` **The " matters**

# Freeing up a port
`taskkill /pid (Get-NetTCPConnection -LocalPort <PORT>).OwningProcess /f`
