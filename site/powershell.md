# Environment variables
Get: `$env:<VAR>`  
Set: `$env:<VAR> = "<VALUE>"` **The " matters**

# Freeing up a port
`Get-NetTCPConnection -LocalPort <PORT>`  
`taskkill /pid <PID> /f`
