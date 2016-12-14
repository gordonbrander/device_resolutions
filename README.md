# Device Resolutions

I haven't been able to find a good programmatically accessible list of devices and resolutions, so I'm compiling one. Contributions welcome.

`device_resolutions.csv` contains entries for device, HW resolution, SW resolution, PPI, primary orientation and can be used to derive screen dimensions and aspect ratio.

## device_resolutions.csv

Devices Covered:

- [x] iPhone (all)
- [x] iPad (all)
- [ ] Mac (soon to be all)
- [ ] Popular Samsung and Samsung Galaxy phones
- [ ] Popular Android tablets
- [ ] Google Nexus
- [ ] Google Pixel
- [ ] Kindle Fire Tablet
- [ ] Kindle Fire phone
- [ ] Standard TV broadcast formats (1080p, 720p, etc)

CSV includes information on `dp` (software pixels), `px` (hardware pixels), primary device orientation and screen measurements.

## aspect_ratios.csv

Aspect ratios covered:

- [x] Common TV
- [x] IMAX
- [x] Cinema
- [x] Common device aspect ratios (16:9, etc)

## More

- [x] Python conversion functions for deriving screen information from CSV
- [ ] Single-page web app visualizing overlayed screen sizes with D3.js
