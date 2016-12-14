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
- [x] Kindle Fire Tablet
- [ ] Kindle Fire Phone
- [ ] Standard TV broadcast formats (1080p, 720p, etc)

CSV includes information on device `dp` (software pixels), `px` (hardware pixels), and screen measurements.

Using this information, you can derive:

- Aspect ratio
- ppi/screen size
- pixel density
- primary orientation (portrait/landscape)

## aspect_ratios.csv

Aspect ratios covered:

- [x] Common TV
- [x] IMAX
- [x] Cinema
- [x] Common device aspect ratios (16:9, etc)

## More

- [x] Python conversion functions for deriving screen information from CSV
- [ ] Single-page web app visualizing overlayed screen sizes with D3.js

## Contributing

Contributions are welcome.

- All contributions should come in the form of pull requests.
- Please include a link to the source/reference for device specifications if possible.
- Be sure to take into consideration the primary orientation of the device (portrait/landscape) and enter width and height accordingly. Width should be the length of the "bottom" of the screen when the device is held in  its primary orientation. Height should be the length of the "side" of the screen when the device is held in its primary orientation. This convention allows primary orientation to be derived from width/height information.