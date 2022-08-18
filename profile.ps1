Set-Alias -Name code -Value "code-insiders";
Set-Alias -Name p -Value "python";
Set-Alias -Name p3 -Value "python3";
Set-Alias -Name ff -Value "ffmpeg";
Set-Alias -Name youtube-dl -Value "yt-dlp";
Set-Alias -Name vim -Value "nvim";
Set-Alias -Name vi -Value "nvim";
Set-Alias -Name which -Value "get-command";
Set-Alias -Name open -Value "explorer";
$env:HTTP_PROXY="http://127.0.0.1:7890";
$env:HTTPS_PROXY="http://127.0.0.1:7890";
$env:ALL_PROXY="http://127.0.0.1:7890";
$env:http_proxy="http://127.0.0.1:7890";
$env:https_proxy="http://127.0.0.1:7890";
$env:all_proxy="http://127.0.0.1:7890";
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
};