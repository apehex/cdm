$files_to_compress = Get-ChildItem -Recurse | Where-Object { $_.Name -match '.*\.(jpg|JPG|jpeg|JPEG|png|PNG|gif|GIF)$' }
[string[]] $paths_to_compress = @()
ForEach ($file in $files_to_compress) {
    $paths_to_compress += $file.FullName
}
Compress-Archive -Path $paths_to_compress -DestinationPath 'images.zip' -CompressionLevel Optimal