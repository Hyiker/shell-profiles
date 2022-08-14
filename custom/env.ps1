function Set-Env {
    param (
        [Parameter(Mandatory=$true)]
        [string]$Key,
        [Parameter(Mandatory=$true)]
        [string]$Value
    )
    gsudo "[System.Environment]::SetEnvironmentVariable('$Key', '$Value', [System.EnvironmentVariableTarget]::Machine)";
    [System.Environment]::SetEnvironmentVariable($Key, $Value);
}

function Remove-Env {
    param (
        [Parameter(Mandatory=$true)]
        [string]$Key
    )
    gsudo "[System.Environment]::SetEnvironmentVariable('$Key', '$null', [System.EnvironmentVariableTarget]::Machine)";
    [System.Environment]::SetEnvironmentVariable($Key, $null);
}