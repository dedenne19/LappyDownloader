#!/bin/bash
APPID="moe.nyarchlinux.lappydownloader"
BUNDLENAME="lappydownloader.flatpak"
flatpak-builder --install --user --force-clean flatpak-app "$APPID".json

if [ "$1" = "bundle" ]; then
	flatpak build-bundle ~/.local/share/flatpak/repo "$BUNDLENAME" "$APPID"
fi
