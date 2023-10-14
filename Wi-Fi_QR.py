import qrcode
ssid = "Wi-Fi_NAME"
password = "PASSWORD"
security_type = "WPA_TYPE_HERE"


wifi_data = f"WIFI:T:{security_type};S:{ssid};P:{password};;"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(wifi_data)
qr.make(fit=True)

qr_img = qr.make_image(fill_color="black", back_color="white")

qr_img.save("Wifi_QR.png")
qr_img.show()

