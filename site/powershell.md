# Environment variables
Get: `$env:<VAR>`  
Set: `$env:<VAR> = "<VALUE>"` **The " matters**

# Freeing up a port
`Get-Process -Id (Get-NetTCPConnection -LocalPort <PORT>).OwningProcess`  
`taskkill /pid <PID> /f`
